import openai


def get_openai_chat_completion(input_prompt, model_name, temp=0.1, timeout=60):
    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": input_prompt}],
        temperature=temp,
        request_timeout=timeout,
    )
    return completion


def get_openai_completion(
    input_prompt, model_name, max_tokens=256, temp=0.1, timeout=60
):
    completion = openai.Completion.create(
        model=model_name,
        prompt=input_prompt,
        max_tokens=max_tokens,
        temperature=temp,
        request_timeout=timeout,
    )
    return completion
