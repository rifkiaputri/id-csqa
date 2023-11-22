import time

from tqdm import tqdm

from ..utils import api


def translate_data(data, src_lang="en", tgt_lang="id"):
    results = []
    for item in tqdm(data):
        trans_items = [item["question"], item["question_concept"]] + item["choices"][
            "text"
        ]

        try:
            trans_texts = api.get_google_translation(
                trans_items, src_lang=src_lang, tgt_lang=tgt_lang
            )
        except Exception:
            print("Caught exception, wait for 1 min...")
            time.sleep(60)
            trans_texts = api.get_google_translation(
                trans_items, src_lang=src_lang, tgt_lang=tgt_lang
            )

        results.append(
            {
                "id": item["id"],
                "question": trans_texts[0],
                "question_concept": trans_texts[1],
                "choices": {"label": item["choices"]["label"], "text": trans_texts[2:]},
                "answerKey": item["answerKey"],
            }
        )

    return results
