import csv
import ast


def load_csv_data(file_path, bool_params):
    # Initialize an empty list to store the data
    data_list = []

    # Open the CSV file for reading
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csvfile)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Append the row (as a dictionary) to the data_list
            row["choices"] = ast.literal_eval(row["choices"])

            for param in bool_params:
                if row[param].lower() == "true":
                    row[param] = True
                elif row[param].lower() == "false":
                    row[param] = False
                else:
                    raise TypeError(f"{param} data cannot be recognized")

            data_list.append(row)

    return data_list


def load_all_csv_data(split, dir_path, file_name, bool_params):
    data = {}

    for s in split:
        file_path = f"{dir_path}/{s}{file_name}"
        data[s] = load_csv_data(file_path, bool_params)
    return data


def save_data(samples, file_path):
    # Get the keys from the first dictionary
    header = samples[0].keys()

    # Write the data to the CSV file
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        # Write the header
        writer.writeheader()

        # Write the data
        for row in samples:
            writer.writerow(row)

    print(f'CSV file "{file_path}" has been created with the data.')


# Function to generate choice text
def generate_choices_text(choices):
    labels = choices["label"]
    texts = choices["text"]

    choice_text = ""
    for idx, label in enumerate(labels):
        choice_text += f'{label}. "{texts[idx]}"\n'

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
