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


def load_gpt_model(model_name, history_version, prompt_type):
    cache = ChatCompletionHistory(model_name, history_version, prompt_type)
    return lambda prompt: cache.query_model(prompt)


def load_open_model(model_name, history_version, prompt_type):
    cache = HfModelHistory(model_name, history_version, prompt_type)
    return lambda prompts: cache.query_model(prompts)


def evaluate_responses(predictions, golds, categories):
    assert len(predictions) == len(golds)
    accuracy = accuracy_score(golds, predictions)
    metrics = {"accuracy": accuracy * 100}
    
    if len(categories) == 0:
        return metrics
    
    # Calculate metrics per categories
    cat_metrics = {}
    for c, p, g in zip(categories, predictions, golds):
        if c in cat_metrics:
            cat_metrics[c]['preds'].append(p)
            cat_metrics[c]['golds'].append(g)
        else:
            cat_metrics[c] = {
                'preds': [p],
                'golds': [g]
            }
    
    for c in set(categories):
        metrics[f"accuracy_{c}"] = accuracy_score(cat_metrics[c]['golds'], cat_metrics[c]['preds']) * 100
    
    return metrics


def extract_data_info(dataset_filename):
    # Define the patterns for language and data name
    lang_pattern = r"(ind|sun)"
    data_pattern = r"(v1_llm_adapt|v2_human_gen|v3_llm_gen)"

    # Search for patterns in the filename
    lang_match = re.search(lang_pattern, dataset_filename)
    data_match = re.search(data_pattern, dataset_filename)

    # Extract the matched groups, default to 'unknown' if not found
    lang = lang_match.group(0) if lang_match else 'unknown'
    data_name = data_match.group(0) if data_match else 'unknown'

    return data_name, lang


def write_evaluation_metrics_to_csv(model_name, dataset_filename, evaluation_metrics, version, prompt_type, out_name):
    filename = f'eval_results/{out_name}'
    file_exists = os.path.exists(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header if the file does not exist
        if not file_exists:
            header = ['Model', 'Dataset Name', 'Lang', 'Version', 'Prompt', 'Accuracy']
            if 'accuracy_history' in evaluation_metrics:
                header += ['Accuracy_History', 'Accuracy_Culture',
                                 'Accuracy_Activity', 'Accuracy_Culinary', 'Accuracy_Place']
            writer.writerow(header)

        # Write the evaluation metrics
        data_name, lang = extract_data_info(dataset_filename)
        metrics_data = [model_name, data_name, lang, version, prompt_type, evaluation_metrics['accuracy']]
        if 'accuracy_history' in evaluation_metrics:
            metrics_data += [evaluation_metrics['accuracy_history'], evaluation_metrics['accuracy_culture'],
                             evaluation_metrics['accuracy_activity'], evaluation_metrics['accuracy_culinary'],
                             evaluation_metrics['accuracy_place']]
        writer.writerow(metrics_data)


def evaluate_model(model, model_name, dataset, batch_size, gold_key, is_gpt, prompt_type, few_shot_data):
    results, golds, categories = [], [], []
    use_prompt_template = "sealion" in model_name and "instruct" in model_name

    for i in tqdm(range(0, len(dataset), batch_size), desc="Evaluating"):
        batch = dataset[i:i + batch_size]
        batch_prompts = [helpers.generate_eval_prompt(item, prompt_type, use_prompt_template, few_shot_data) for item in batch]
        batch_golds = [item[gold_key] for item in batch]
        if 'category' in batch[0]:
            batch_categories = [item['category'] for item in batch]
        else:
            batch_categories = []

        if is_gpt:
            responses = [model(prompt) for prompt in batch_prompts]
        else:
            responses = model(batch_prompts)

        results.extend(zip(batch_prompts, responses))
        golds.extend(batch_golds)
        categories.extend(batch_categories)

    evaluation_metrics = evaluate_responses([response for _, response in results], golds, categories)

    return results, evaluation_metrics


def main(args):
    dataset = load_dataset(args.dataset_path)

    if "gpt" in args.model_name:
        model = load_gpt_model(args.model_name, args.history_version, args.prompt_type)
        is_gpt = True
    else:
        model = load_open_model(args.model_name, args.history_version, args.prompt_type)
        is_gpt = False

    if not args.few_shot:
        few_shot_data = None
    else:
        print("Load few-shot data...")
        _, lang = extract_data_info(args.dataset_path)
        if lang == "ind":
            few_shot_data = helpers.load_json_data("../dataset/v1_adapt/ind/train_3_shot.json")
        elif lang == "sun":
            few_shot_data = helpers.load_json_data("../dataset/v1_adapt/ind/train_3_shot.json")
        else:
            print("Few shot data not found.")
            few_shot_data = None

    evaluation_results, evaluation_metrics = evaluate_model(
        model=model,
        model_name=args.model_name,
        dataset=dataset,
        batch_size=args.batch_size,
        gold_key=args.gold_key,
        is_gpt=is_gpt,
        prompt_type=args.prompt_type,
        few_shot_data=few_shot_data
    )

    print("Evaluation complete.")
    print("Evaluation Example:")
    print(f"[INPUT PROMPT] {evaluation_results[0][0]}")
    print(f"[RESPONSE] {evaluation_results[0][1]}")
    print("Evaluation Metrics:", evaluation_metrics)

    print("Write evaluation metrics...")
    write_evaluation_metrics_to_csv(
        args.model_name,
        args.dataset_path,
        evaluation_metrics,
        args.history_version,
        args.prompt_type,
        args.out_name
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", help="name of the model to be tested", required=True, type=str)
    parser.add_argument("--dataset_path", help="path to the testing dataset", required=True, type=str)
    parser.add_argument("--out_name", help="file name of the evaluation output", required=True, type=str)
    parser.add_argument("--gold_key", help="key for gold answer", required=True, type=str)
    parser.add_argument("--history_version", help="history file version (only for GPT models)", required=False, type=str)
    parser.add_argument("--batch_size", help="eval batch size", required=True, type=int)
    parser.add_argument("--prompt_type", help="prompt type", required=True, type=int)
    parser.add_argument("--few_shot", help="whether to add 3-shot examples or not", action='store_true')
    args = parser.parse_args()

    main(args)
