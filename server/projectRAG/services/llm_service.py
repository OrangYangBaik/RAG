from openai import OpenAI
from config.settings import LOCAL_LLM_API

def extract_response_after_think(text):
    if "</think>" in text:
        return text.split("</think>", 1)[1].strip()
    return text.strip()

def call_llm(prompt):
    client = OpenAI(
        base_url=LOCAL_LLM_API["base_url"],
        api_key=LOCAL_LLM_API["api_key"]
    )

    response = client.chat.completions.create(
        model=LOCAL_LLM_API["model_LLM"],
        messages=[
            {"role": "system", "content": "You are a specialist in recommendation service. Give the user recommendations based on the context. Give the answer in english"},
            {"role": "user", "content": prompt}
        ]
    )

    clean_answer = extract_response_after_think(response.choices[0].message.content)
    return clean_answer
