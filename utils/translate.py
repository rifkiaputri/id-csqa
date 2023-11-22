import time

from google.cloud import translate
from tqdm import tqdm


def translate_texts(texts, project_id=None, src_lang="en", tgt_lang="id"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": texts,
            "mime_type": "text/plain",
            "source_language_code": src_lang,
            "target_language_code": tgt_lang,
        }
    )

    return [t.translated_text for t in response.translations]


def translate_data(data, project_id=None, src_lang="en", tgt_lang="id"):
    results = []
    for item in tqdm(data):
        trans_items = [item["question"], item["question_concept"]] + item["choices"][
            "text"
        ]

        try:
            trans_texts = translate_texts(
                trans_items, project_id=project_id, src_lang=src_lang, tgt_lang=tgt_lang
            )
        except Exception:
            print("Caught exception, wait for 1 min...")
            time.sleep(60)
            trans_texts = translate_texts(
                trans_items, project_id=project_id, src_lang=src_lang, tgt_lang=tgt_lang
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
