import os
import sys
import csv
import re
import argparse

from dotenv import load_dotenv
load_dotenv()

from sklearn.metrics import accuracy_score
from tqdm import tqdm

script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

from model import ChatCompletionHistory, HfModelHistory
from utils import helpers


def load_dataset(input_path):
    load_functions = {
        'csv': lambda path: helpers.load_csv_data(path, []),
        'json': helpers.load_json_data
    }
    
    file_ext = input_path.split('.')[-1]
    if file_ext in load_functions:
        return load_functions[file_ext](input_path)
    else:
        raise ValueError(f"Unsupported file extension: {file_ext}")


def load_gpt_model(model_name, history_version):
    cache = ChatCompletionHistory(model_name, history_version)
    return lambda prompt: cache.query_model(prompt)


def load_open_model(model_name, history_version):
    cache = HfModelHistory(model_name, history_version)
    return lambda prompts: cache.query_model(prompts)


def evaluate_responses(predictions, golds):
    assert len(predictions) == len(golds)
    accuracy = accuracy_score(golds, predictions)
    return {"accuracy": accuracy * 100}


def extract_data_info(dataset_filename):
    # Define the patterns for language and data name
    lang_pattern = r"(ind|sun)"
    data_pattern = r"(v1_adapt|v2_human)"

    # Search for patterns in the filename
    lang_match = re.search(lang_pattern, dataset_filename)
    data_match = re.search(data_pattern, dataset_filename)

    # Extract the matched groups, default to 'unknown' if not found
    lang = lang_match.group(0) if lang_match else 'unknown'
    data_name = data_match.group(0) if data_match else 'unknown'

    return data_name, lang


def write_evaluation_metrics_to_csv(model_name, dataset_filename, evaluation_metrics, version, prompt_type):
    filename = 'eval_results/evaluation_metrics.csv'
    file_exists = os.path.exists(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header if the file does not exist
        if not file_exists:
            writer.writerow(['Model', 'Dataset Name', 'Lang', 'Version', 'Prompt', 'Accuracy'])

        # Write the evaluation metrics'
        data_name, lang = extract_data_info(dataset_filename)
        writer.writerow([model_name, data_name, lang, version, prompt_type, evaluation_metrics['accuracy']])


def evaluate_model(model, model_name, dataset, batch_size, gold_key, is_gpt, prompt_type):
    results, golds = [], []
    use_prompt_template = "sealion" in model_name and "instruct" in model_name

    for i in tqdm(range(0, len(dataset), batch_size), desc="Evaluating"):
        batch = dataset[i:i + batch_size]
        batch_prompts = [helpers.generate_eval_prompt(item, prompt_type, use_prompt_template) for item in batch]
        batch_golds = [item[gold_key] for item in batch]

        if is_gpt:
            responses = [model(prompt) for prompt in batch_prompts]
        else:
            responses = model(batch_prompts)

        results.extend(zip(batch_prompts, responses))
        golds.extend(batch_golds)

    evaluation_metrics = evaluate_responses([response for _, response in results], golds)

    return results, evaluation_metrics


def main(args):
    dataset = load_dataset(args.dataset_path)

    if "gpt" in args.model_name:
        model = load_gpt_model(args.model_name, args.history_version)
        is_gpt = True
    else:
        model = load_open_model(args.model_name, args.history_version)
        is_gpt = False

    evaluation_results, evaluation_metrics = evaluate_model(
        model=model,
        model_name=args.model_name,
        dataset=dataset,
        batch_size=args.batch_size,
        gold_key=args.gold_key,
        is_gpt=is_gpt,
        prompt_type=args.prompt_type
    )

    print("Evaluation complete.")
    print("Evaluation Example:")
    print(f"[INPUT PROMPT] {evaluation_results[0][0]}")
    print(f"[RESPONSE] {evaluation_results[0][1]}")
    print("Evaluation Metrics:", evaluation_metrics)

    write_evaluation_metrics_to_csv(args.model_name, args.dataset_path, evaluation_metrics, args.history_version, args.prompt_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", help="name of the model to be tested", required=True, type=str)
    parser.add_argument("--dataset_path", help="path to the testing dataset", required=True, type=str)
    parser.add_argument("--gold_key", help="key for gold answer", required=True, type=str)
    parser.add_argument("--history_version", help="history file version (only for GPT models)", required=False, type=str)
    parser.add_argument("--batch_size", help="eval batch size", required=True, type=int)
    parser.add_argument("--prompt_type", help="prompt type", required=True, type=int)
    args = parser.parse_args()

    main(args)
