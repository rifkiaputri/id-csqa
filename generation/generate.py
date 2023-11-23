import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv

load_dotenv()

import rephrase

from translate import translate_data
from filter import filter_data

from utils import helpers


def create_output_dir():
    out_path = os.getenv("OUTPUT_PATH")
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


split = ["validation", "test", "train"]

if __name__ == "__main__":
    raw_data = helpers.load_all_csv_data(
        split, os.getenv("RAW_DATA_PATH"), ".csv", ["name"]
    )
    create_output_dir()
    id_data = rephrase.rephrase_data(raw_data, split)
    out_path = os.getenv("OUTPUT_PATH")
    for s in split:
        print(f"Translating data split {s}, ID -> SU")
        su_data = translate_data(id_data[s], src_lang="id", tgt_lang="su")

        print(f"Backtranslation for SU -> ID {s}")
        su_id_data = translate_data(su_data, src_lang="su", tgt_lang="id")

        kept_idx = filter_data(id_data[s], su_data, su_id_data)

        filtered_id = [helpers.remove_unused_keys(id_data[s][i]) for i in kept_idx]
        filtered_su = [helpers.remove_unused_keys(su_data[i]) for i in kept_idx]

        helpers.save_data(su_id_data, f"./{out_path}/backtranslation/{s}_su-id.csv")

        unfiltered_dir = f"{out_path}/unfiltered"
        helpers.save_data(id_data[s], f"{unfiltered_dir}/id/{s}_unfiltered_id.csv")
        helpers.save_data(su_data, f"{unfiltered_dir}/su/{s}_unfiltered_su.csv")

        filtered_dir = f"{out_path}/filtered"
        helpers.save_data(filtered_id, f"{filtered_dir}/id/{s}_filtered_id.csv")
        helpers.save_data(filtered_su, f"{filtered_dir}/su/{s}_filtered_su.csv")
