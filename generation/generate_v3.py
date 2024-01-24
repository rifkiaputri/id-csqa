import os
import ast
import sys
import time
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

from utils import api, helpers
from filter import filter_concept_strict


def load_concepts(raw_data_path):
    raw_data = helpers.load_json_data(raw_data_path)
    data = []
    for _, raw in raw_data.items():
        data.extend(raw)

    concepts = {}
    for d in data:
        if d["category"] not in concepts.keys():
            concepts[d["category"]] = [d["question_concept"].lower()]
        else:
            concepts[d["category"]].append(d["question_concept"].lower())

    return concepts


def postprocess_data(response, category):
    response["category"] = category
    response["choices"] = {
        "label": list(response["choices"].keys()),
        "text": list(response["choices"].values()),
    }
    response["answer_majority"] = response["answer_creator"]

    return response


def generate_one_data(concepts, history, cat, lang="id"):
    if lang == "id":
        input_prompt = helpers.generate_id_synthetic_gen_prompt(concepts, cat)
    elif lang == "su":
        input_prompt = helpers.generate_su_synthetic_gen_prompt(concepts, cat)

    if input_prompt in history.keys():
        return input_prompt, history[input_prompt]["response"]

    model_name = "gpt-4-1106-preview"
    try:
        completion = api.get_openai_chat_completion(input_prompt, model_name)
    except Exception:
        print("Caught exception, wait for 1 min...")
        time.sleep(60)
        completion = api.get_openai_chat_completion(input_prompt, model_name)
    response = completion.choices[0].message.content.strip()

    return input_prompt, response


def generate_all_data(concepts, history, history_path, lang="id"):
    generated_data = []
    for category, list_concept in concepts.items():
        list_concept_ = [f'"{c}"' for c in list_concept]
        chunks = helpers.divide_list_into_chunks(list_concept_, 5)

        for chunk in tqdm(chunks):
            prompt, response = generate_one_data(chunk, history, category, lang=lang)
            history[prompt] = {"response": response}
            helpers.save_response_history(history, history_path)

            if "```json" in response:
                response = "\n".join(response.split("\n")[1:-1])

            response = ast.literal_eval(response)
            response = [postprocess_data(r, category) for r in response]
            generated_data.extend(response)

    return generated_data


def filter_data(raw_data):
    filtered_data = []
    for data in raw_data:
        if filter_concept_strict(data):
            filtered_data.append(data)

    return filtered_data


def main(args):
    id_concepts = load_concepts(f"{args.raw_data_path}/ind/raw_test.json")
    su_concepts = load_concepts(f"{args.raw_data_path}/sun/raw_test.json")

    os.makedirs(args.output_path, exist_ok=True)

    history_path = f"{args.output_path}/history.csv"
    response_history = helpers.load_response_history(history_path)
    raw_id_data = generate_all_data(
        id_concepts, response_history, history_path, lang="id"
    )
    raw_su_data = generate_all_data(
        su_concepts, response_history, history_path, lang="su"
    )

    helpers.save_json_data(raw_id_data, f"{args.output_path}/raw_ind.json")
    helpers.save_json_data(raw_su_data, f"{args.output_path}/raw_sun.json")

    filtered_id = filter_data(raw_id_data)
    filtered_su = filter_data(raw_su_data)

    helpers.save_json_data(filtered_id, f"{args.output_path}/filtered_ind.json")
    helpers.save_json_data(filtered_su, f"{args.output_path}/filtered_sun.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output_path",
        help="path to the output directory",
        default="./../dataset/v3_llm_gen",
        type=str,
    )
    parser.add_argument(
        "--raw_data_path",
        help="path to the v2 human data directory",
        default="./../dataset/v2_human_gen",
        type=str,
    )
    parser.add_argument(
        "--model",
        help="openai model used for generation",
        default="gpt-4-1106-preview",
        type=str,
    )
    args = parser.parse_args()

    main(args)
