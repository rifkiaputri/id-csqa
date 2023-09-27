import csv
import ast
import torch
import torchaudio

from glob import glob
from tqdm import tqdm
from seamless_communication.models.inference import Translator


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

    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in samples:
            writer.writerow(row)

    print(f'CSV file "{file_path}" has been created with the data.')


model = "seamlessM4T_large"
vocoder_model = "vocoder_36langs"

translator = Translator(model, vocoder_model, torch.device("cpu"), torch.float16)

for folder in glob("./eval/*/"):
    for file in glob(f"{folder}*.csv"):
        if "v3_test_name" in file:
            fname = file.split("/")[-1]
            print(f"Translating file {fname}")

            file_data = load_csv_data(file)
            for data in tqdm(file_data):
                question, _, _ = translator.predict(
                    data["question"],
                    "t2tt",
                    "ind",
                    src_lang="eng",
                    ngram_filtering=True,
                )
                data["question"] = str(question)

                concept, _, _ = translator.predict(
                    data["question_concept"],
                    "t2tt",
                    "ind",
                    src_lang="eng",
                    ngram_filtering=True,
                )
                data["question_concept"] = str(concept).lower()

                for i in range(len(data["choices"]["text"])):
                    opt = data["choices"]["text"][i]
                    opt_text, _, _ = translator.predict(
                        opt, "t2tt", "ind", src_lang="eng", ngram_filtering=True
                    )
                    data["choices"]["text"][i] = str(opt_text).lower()

            translated_file = f"{folder}sm4t_large/translated_sm4t_large_{fname}"
            save_data(file_data, translated_file)
