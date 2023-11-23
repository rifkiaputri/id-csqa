import os

from dotenv import load_dotenv

load_dotenv()
load_dotenv("../.env.rephrase")

import rephrase

from translate import translate_data
from filter import filter_data

from ..utils import helpers

split = ["validation", "test", "train"]

if __name__ == "__main__":
    raw_data = helpers.load_all_csv_data(
        split, os.getenv("RAW_DATA_PATH"), ".csv", ["name"]
    )
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

        helpers.save_data(id_data[s], f"{out_path}/{s}_rephrased_id.csv")
        helpers.save_data(su_data, f"./{out_path}/{s}_rephrased_su.csv")
        helpers.save_data(su_id_data, f"./{out_path}/{s}_backtranslation_su-id.csv")

        helpers.save_data(filtered_id, f"{out_path}/{s}_filtered_id.csv")
        helpers.save_data(filtered_su, f"./{out_path}/{s}_filtered_su.csv")
