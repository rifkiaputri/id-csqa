import os
import ast
import time
import pandas as pd

from tqdm import tqdm

from ..utils import helpers, api


def clean_data(data):
    letters = {"a", "b", "c", "d", "e"}
    alt_letters = {"b", "c", "d", "e", "f"}

    options = data["choices"]["text"]
    labels = set([option[0].lower() for option in options])

    if labels == letters or labels == alt_letters:
        options = [option[4:] if option[3] == '"' else option[3:] for option in options]

    options = [option.replace('"', "") for option in options]
    data["choices"]["text"] = options

    return data


def clean_response_keys(response):
    if "question" not in list(response.keys()):
        if "Question" in list(response.keys()):
            response["question"] = response["Question"]
        elif "pertanyaan" in list(response.keys()):
            response["question"] = response["pertanyaan"]
        else:
            raise ValueError(f"Response is not right: {response}")

    if "concept" not in list(response.keys()):
        if "Concept" in list(response.keys()):
            response["concept"] = response["Concept"]
        elif "konsep" in list(response.keys()):
            response["concept"] = response["konsep"]
        else:
            raise ValueError(f"Response is not right: {response}")

    if "options" not in list(response.keys()):
        if "Options" in list(response.keys()):
            response["options"] = response["Options"]
        elif "opsi" in list(response.keys()):
            response["options"] = response["opsi"]
        else:
            raise ValueError(f"Response is not right: {response}")

    if "question_answer" not in list(response.keys()):
        if "Question Answer" in list(response.keys()):
            response["question_answer"] = response["Question Answer"]
        elif "Question_Answer" in list(response.keys()):
            response["question_answer"] = response["Question_Answer"]
        elif "jawaban_pertanyaan" in list(response.keys()):
            response["question_answer"] = response["jawaban_pertanyaan"]
        else:
            raise ValueError(f"Response is not right: {response}")

    return response


def postprocess_result_all(data, response):
    if "```json" in response:
        response = "\n".join(response.split("\n")[1:-1])

    rephrased_result = clean_response_keys(ast.literal_eval(response))
    letters = ["A", "B", "C", "D", "E"]

    if isinstance(rephrased_result["options"], list):
        if len(rephrased_result["options"]) == 5:
            rephrased_result["options"] = dict(
                zip(letters, rephrased_result["options"])
            )
        else:
            option_labels = [
                option[0].lower() for option in rephrased_result["options"]
            ]
            if set(option_labels).issubset(set([l.lower() for l in letters])):
                option_texts = [
                    option[4:] if option[3] == '"' else option[3:]
                    for option in rephrased_result["options"]
                ]
                label_not_in_option = [
                    label.upper()
                    for label in list(
                        set([l.lower() for l in letters]) - set(option_labels)
                    )
                ]
                for label in label_not_in_option:
                    chosen_idx = data["choices"]["label"].index(label)
                    chosen_text = data["choices"]["text"][chosen_idx]
                    option_texts.insert(chosen_idx, chosen_text)

                rephrased_result["options"] = dict(zip(letters, option_texts))
            else:
                raise ValueError(
                    f"Option output is not right: {rephrased_result['options']}"
                )

    answer = rephrased_result["question_answer"]
    if len(answer) > 1 and answer[0].lower() not in [l.lower() for l in letters]:
        option_texts = [
            text.lower() for text in list(rephrased_result["options"].values())
        ]
        if rephrased_result["question_answer"].lower() in option_texts:
            option_labels = list(rephrased_result["options"].keys())
            answer_idx = option_texts.index(rephrased_result["question_answer"].lower())
            rephrased_result["question_answer"] = option_labels[answer_idx]
        else:
            raise ValueError(
                f"Answer key not in options: {rephrased_result['question_answer']}"
            )
    else:
        rephrased_result["question_answer"] = rephrased_result["question_answer"][0]

    return rephrased_result


def postprocess_result_name(response):
    if "Question: " in response:
        rephrased_result = response.split("Question: ")[-1]
    else:
        rephrased_result = response

    return rephrased_result


def save_response_history(response_history, history_path):
    resp_history_df = pd.DataFrame(
        {
            "prompt": response_history.keys(),
            "response": response_history.values(),
        }
    )
    resp_history_df.to_csv(history_path, index=False)


def generate_rephrased_data(data, model_name, history, prompt_type="all"):
    if prompt_type == "all":
        input_prompt = helpers.generate_rephrase_all_prompt(data)
    elif prompt_type == "name":
        input_prompt = helpers.generate_rephrase_name_prompt(data)
    else:
        raise ValueError(f"prompt_type is not right: {prompt_type}")

    if input_prompt in history.keys():
        return input_prompt, history[input_prompt]["response"]

    try:
        completion = api.get_openai_chat_completion(input_prompt, model_name)
    except Exception:
        print("Caught exception, wait for 1 min...")
        time.sleep(60)
        completion = api.get_openai_chat_completion(input_prompt, model_name)
    response = completion.choices[0].message.content.strip()  # type: ignore

    return input_prompt, response


def rephrase_data(raw_data, split):
    out_path = os.environ.get("OUTPUT_PATH")

    rephrased_results = {}
    for s in split:
        print(f"Process data on split: {s}")

        history_path = f"{out_path}/{s}_history.csv"
        if os.path.exists(history_path):
            print(f"Load response history from file {history_path}")
            resp_history_df = pd.read_csv(
                history_path, converters={"response": lambda x: ast.literal_eval(x)}
            )
            response_history = dict(
                zip(resp_history_df.prompt, resp_history_df.response)
            )
        else:
            print(f"Initialize response history")
            response_history = {}

        rephrased_result = []
        for data in tqdm(raw_data[s]):
            rephrased_data = data.copy()

            # Rephrase All
            prompt, response = generate_rephrased_data(
                data,
                os.environ.get("REPHRASE_ALL_MODEL"),
                response_history,
                prompt_type="all",
            )
            response_history[prompt] = {"response": response}
            save_response_history(response_history, history_path)

            result = postprocess_result_all(data, response)

            # Rephrase name if name=True
            if data["name"]:
                prompt, response = generate_rephrased_data(
                    data,
                    os.environ.get("REPHRASE_NAME_MODEL"),
                    response_history,
                    prompt_type="name",
                )
                save_response_history(response_history, history_path)
                result["question"] = postprocess_result_name(response)

            rephrased_data["question"] = result["question"]
            rephrased_data["choices"] = {
                "label": list(result["options"].keys()),
                "text": [text.lower() for text in list(result["options"].values())],
            }

            if "concept" in list(result.keys()):
                rephrased_data["question_concept"] = result["concept"]

            rephrased_data["answerKey"] = result["question_answer"]
            rephrased_result.append(clean_data(rephrased_data))

        rephrased_results[s] = rephrased_result
        helpers.save_data(rephrased_result, f"{out_path}/{s}_rephrased_id.csv")

    return rephrased_results
