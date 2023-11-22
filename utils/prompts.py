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
