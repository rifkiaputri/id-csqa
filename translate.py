import os
import csv
import ast

# import torch
# import torchaudio

from glob import glob
from tqdm import tqdm

# from seamless_communication.models.inference import Translator

from googletrans import Translator as gtrans

model = "seamlessM4T_medium"
vocoder_model = "vocoder_36langs"

# sm4t_translator = Translator(model, vocoder_model, torch.device("cuda"), torch.float16)
sm4t_translator = None
google_translator = gtrans(service_urls=["translate.google.co.id"])


def load_csv_data(file_path):
    data_list = []

    with open(file_path, newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            row["choices"] = ast.literal_eval(row["choices"])
            data_list.append(row)

    return data_list


def save_data(samples, file_path):
    header = samples[0].keys()

    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in samples:
            writer.writerow(row)

    print(f'CSV file "{file_path}" has been created with the data.')


def generate_translate_text(row):
    # return row["question"]
    return f"""
Question: {row['question']}
Concept: {row['question_concept']}
Options: {', '.join(row['choices']['text'])}"""


def translate_sm4t(data):
    question, _, _ = sm4t_translator.predict(
        data["question"],
        "t2tt",
        "ind",
        src_lang="eng",
        ngram_filtering=True,
    )
    data["question"] = str(question)

    concept, _, _ = sm4t_translator.predict(
        data["question_concept"],
        "t2tt",
        "ind",
        src_lang="eng",
        ngram_filtering=True,
    )
    data["question_concept"] = str(concept).lower()

    for i in range(len(data["choices"]["text"])):
        opt = data["choices"]["text"][i]
        opt_text, _, _ = sm4t_translator.predict(
            opt, "t2tt", "ind", src_lang="eng", ngram_filtering=True
        )
        data["choices"]["text"][i] = str(opt_text).lower()

    return data


def translate_google(data, lang_dest):
    text2translate = generate_translate_text(data)

    if "id" in lang_dest:
        translated = google_translator.translate(
            text2translate, src="en", dest="id"
        ).text

    if lang_dest == "su":
        translated = google_translator.translate(
            text2translate, src="en", dest="su"
        ).text

    if lang_dest == "gpt_su":
        translated = google_translator.translate(
            text2translate, src="id", dest="su"
        ).text

    if lang_dest == "idsu":
        translated = google_translator.translate(translated, src="id", dest="su").text

    response = translated.split("\n")
    new_data = {}
    new_data["question"] = str(response[0].split(": ")[-1])
    new_data["question_concept"] = str(response[1].split(": ")[-1]).lower()
    new_data["options"] = response[2].split(": ")[-1].lower().split(", ")

    return new_data


for folder in glob("./eval/*/"):
    os.makedirs(f"{folder}google/", exist_ok=True)

    for file in glob(f"{folder}*.csv"):
        fname = file.split("/")[-1]
        if "v3" in fname and "eval" not in fname:
            print(f"Translating file {fname}")

            file_data = load_csv_data(
                f"{folder}chatgpt-instruct/translated_chatgpt_instruct_{fname}"
            )
            result = []
            for data in tqdm(file_data[:5]):
                result.append(translate_google(data, "gpt_su"))

            translated_file = f"{folder}google/translated_google_gpt_idsu_{fname}"
            save_data(result, translated_file)
