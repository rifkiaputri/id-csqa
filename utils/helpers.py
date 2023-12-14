import os
import csv
import ast
import json

import pandas as pd


def remove_unused_keys(
    data, used_keys=["id", "question", "question_concept", "choices", "answerKey"]
):
    return {k: v for k, v in data.items() if k in used_keys}


def divide_list_into_chunks(input_list, chunk_size):
    return [
        input_list[i : i + chunk_size] for i in range(0, len(input_list), chunk_size)
    ]


def create_output_dir(out_path):
    os.makedirs(f"{out_path}", exist_ok=True)

    os.makedirs(f"{out_path}/response_history", exist_ok=True)
    os.makedirs(f"{out_path}/backtranslation", exist_ok=True)

    unfiltered_dir = f"{out_path}/unfiltered"
    os.makedirs(unfiltered_dir, exist_ok=True)
    os.makedirs(f"{unfiltered_dir}/id", exist_ok=True)
    os.makedirs(f"{unfiltered_dir}/su", exist_ok=True)

    filtered_dir = f"{out_path}/filtered"
    os.makedirs(filtered_dir, exist_ok=True)
    os.makedirs(f"{filtered_dir}/id", exist_ok=True)
    os.makedirs(f"{filtered_dir}/su", exist_ok=True)


def load_csv_data(file_path, bool_params):
    # Initialize an empty list to store the data
    data_list = []

    # Open the CSV file for reading
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csvfile)

        # Iterate through each data in the CSV file
        for data in csv_reader:
            # Append the data (as a dictionary) to the data_list
            data["choices"] = ast.literal_eval(data["choices"])

            for param in bool_params:
                if data[param].lower() == "true":
                    data[param] = True
                elif data[param].lower() == "false":
                    data[param] = False
                else:
                    raise TypeError(f"{param} data cannot be recognized")

            data_list.append(data)

    return data_list


def load_all_csv_data(split, dir_path, file_name, bool_params):
    all_data = {}

    for s in split:
        file_path = f"{dir_path}/{s}{file_name}"
        all_data[s] = load_csv_data(file_path, bool_params)

    return all_data


def save_data(data_list, file_path):
    if len(data_list) == 0:
        print(f'CSV file "{file_path}" has not been created, data is empty')
        return

    # Get the keys from the first dictionary
    header = data_list[0].keys()

    # Write the data to the CSV file
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        # Write the header
        writer.writeheader()

        # Write the data
        for data in data_list:
            writer.writerow(data)

    print(f'CSV file "{file_path}" has been created with the data.')


def load_json_data(file_path):
    with open(file_path, encoding="utf-8") as fp:
        dataset = json.load(fp)
    return dataset


def save_json_data(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_response_history(history_path):
    if os.path.exists(history_path):
        print(f"Load response history from file {history_path}")
        resp_history_df = pd.read_csv(
            history_path, converters={"response": lambda x: ast.literal_eval(x)}
        )
        response_history = dict(zip(resp_history_df.prompt, resp_history_df.response))
    else:
        print(f"Initialize response history")
        response_history = {}

    return response_history


def save_response_history(response_history, history_path):
    resp_history_df = pd.DataFrame(
        {
            "prompt": response_history.keys(),
            "response": response_history.values(),
        }
    )
    resp_history_df.to_csv(history_path, index=False)


def generate_input_text(data):
    return " ".join(
        [data["question"], data["question_concept"]] + data["choices"]["text"]
    )


# Function to generate choice text
def generate_choices_text(choices, with_quote=True):
    labels = choices["label"]
    texts = choices["text"]

    choice_text = ""
    for idx, label in enumerate(labels):
        if with_quote:
            choice_text += f'{label}. "{texts[idx]}"\n'
        else:
            choice_text += f"{label}. {texts[idx]}\n"

    return choice_text


# Function to generate answer text
def generate_answer_text(choices, answerKey):
    idx = choices["label"].index(answerKey)
    answer_text = f'{answerKey}. "{choices["text"][idx]}"'

    return answer_text


# Function to generate prompts based on the conditions
def generate_rephrase_all_prompt(data):
    return f"""Change the given data to make it relevant to Indonesia in any ways. Make all elements relevant to each other, and the concept always appear explicitly in the question. Return in Indonesian language with JSON format where question is string, concept is string, options is dictionary where label is the keys and option text is the values, and question_answer is string contain one label from the options.

Data:
###
Question: {data['question']}
Concept: {data['question_concept']}
Options:
{generate_choices_text(data['choices'])}Question Answer: {generate_answer_text(data['choices'], data['answerKey']) if data['answerKey'] else ''}
###

Changed data in JSON:"""


# Function to generate prompts based on the conditions
def generate_rephrase_name_prompt(data):
    return f"""Change all names in the given question to Indonesian names. Change only the names, keep all other phrases in the question the same and keep it all in Indonesian.

Question: {data['question']}
Changed Question:"""


# Function to generate prompts for benchmarking/evaluation based on prompt_type
def generate_eval_prompt(data, prompt_type=1):
    if prompt_type == 1:  # adapted from MMLU prompt
        if "question_concept" in data:
            concept = data["question_concept"].strip()
        elif "question_concepts" in data:
            concept = data["question_concepts"].strip()
        else:
            raise Exception(f"Question concept not found for: {data}")

        return f"""The following are multiple choice questions (with answers) about \"{concept}\".
{data['question'].strip()}
{generate_choices_text(data['choices'], with_quote=False).strip()}
Answer:"""
    elif prompt_type == 2:  # adapted from AI harness prompt
        return f"""Question: {data['question'].strip()}
Choices:
{generate_choices_text(data['choices'], with_quote=False).strip()}
Answer:"""
    elif prompt_type == 3:  # adapted from HELM prompt
        if "question_concept" in data:
            concept = data["question_concept"].strip()
        elif "question_concepts" in data:
            concept = data["question_concepts"].strip()
        else:
            raise Exception(f"Question concept not found for: {data}")

        return f"""The following are multiple choice questions (with answers) about \"{concept}\".

Question: {data['question'].strip()}
{generate_choices_text(data['choices'], with_quote=False).strip()}
Answer:"""
    else:
        raise NotImplementedError(f"Not implemented for prompt_type: {prompt_type}")


def generate_id_synthetic_gen_prompt(concepts, cat):
    return f"""Given a list of Indonesian concepts [{', '.join(concepts)}], create one Indonesian commonsense QA data with topic "{cat}" for each concept, that consists of three components: "question", "choices", and "answer_creator". The "question" must contains the concept explicitly. The "choices" consist of 5 different choices marked A to E where one should be the "answer_creator". All data should be in Indonesian, return only your answer in JSON data format, and add the concept of the data as "question_concepts".

JSON Data:"""


def generate_su_synthetic_gen_prompt(concepts, cat):
    return f"""Given a list of Sundanese concepts [{', '.join(concepts)}], create one Sundanese commonsense QA data with topic "{cat}" for each concept, that consists of three components: "question", "choices", and "answer_creator". The "question" must contains the concept explicitly. The "choices" consist of 5 different choices marked A to E where one should be the "answer_creator". All data should be in Sundanese, return only your answer in JSON data format, and add the concept of the data as "question_concepts".

JSON Data:"""


def generate_combined_synthetic_gen_prompt(id_concepts, su_concepts, cat):
    return f"""Given a list of Indonesian concepts [{', '.join(id_concepts)}] and Sundanese concepts [{', '.join(su_concepts)}], create one commonsense QA data with topic "{cat}" for each concept, that consists of three components: "question", "choices", and "answer_creator". The "question" must contains the concept explicitly. The "choices" consist of 5 different choices marked A to E where one should be the "answer_creator". All data should be in Indonesian or Sundanese based on the concept, return only your answer in JSON data format, and add the concept of the data as "question_concepts".

JSON Data:"""
