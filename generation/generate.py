import os
import sys
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv

load_dotenv()

import rephrase

from translate import translate_data
from filter import filter_data

from utils import helpers


parser = argparse.ArgumentParser()
parser.add_argument(
    "--output_path", help="path to the output directory", required=True, type=str
)
parser.add_argument(
    "--raw_data_path", help="path to the raw data directory", required=True, type=str
)
parser.add_argument(
    "--rephrase_all_model",
    help="openai model used for rephrase all",
    default="gpt-4-1106-preview",
    type=str,
)
parser.add_argument(
    "--rephrase_name_model",
    help="openai model used for rephrase name",
    default="gpt-3.5-turbo",
    type=str,
)
parser.add_argument(
    "--translation_threshold",
    help="threshold for translation filter",
    default=0.9,
    type=float,
)
args = parser.parse_args()

split = ["validation", "test", "train"]

if __name__ == "__main__":
    raw_data = helpers.load_all_csv_data(split, args.raw_data_path, ".csv", ["name"])
    helpers.create_output_dir(args.output_path)
    id_data = rephrase.rephrase_data(
        raw_data,
        split,
        args.output_path,
        args.rephrase_all_model,
        args.rephrase_name_model,
    )

    for s in split:
        print(f"Translating data split {s}, ID -> SU")
        su_data = translate_data(id_data[s], src_lang="id", tgt_lang="su")

        print(f"Backtranslation for SU -> ID {s}")
        su_id_data = translate_data(su_data, src_lang="su", tgt_lang="id")

        kept_idx = filter_data(
            id_data[s], su_data, su_id_data, args.translation_threshold
        )

        filtered_id = [helpers.remove_unused_keys(id_data[s][i]) for i in kept_idx]
        filtered_su = [helpers.remove_unused_keys(su_data[i]) for i in kept_idx]

        helpers.save_data(
            su_id_data, f"./{args.output_path}/backtranslation/{s}_su-id.csv"
        )

        unfiltered_dir = f"{args.output_path}/unfiltered"
        helpers.save_data(id_data[s], f"{unfiltered_dir}/id/{s}_unfiltered_id.csv")
        helpers.save_data(su_data, f"{unfiltered_dir}/su/{s}_unfiltered_su.csv")

        filtered_dir = f"{args.output_path}/filtered"
        helpers.save_data(filtered_id, f"{filtered_dir}/id/{s}_filtered_id.csv")
        helpers.save_data(filtered_su, f"{filtered_dir}/su/{s}_filtered_su.csv")
