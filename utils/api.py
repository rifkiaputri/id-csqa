import os

from openai import OpenAI
from google.cloud import translate

client = OpenAI()


def get_openai_chat_completion(input_prompt, model_name, temp=0.1):
    completion = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": input_prompt}],
        temperature=temp,
    )
    return completion


def get_openai_completion(input_prompt, model_name, max_tokens=256, temp=0.1):
    completion = client.completions.create(
        model=model_name,
        prompt=input_prompt,
        max_tokens=max_tokens,
        temperature=temp,
    )
    return completion


def get_google_translation(texts, src_lang="en", tgt_lang="id"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{os.environ.get('GOOGLE_PROJECT_ID')}/locations/{location}"

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
