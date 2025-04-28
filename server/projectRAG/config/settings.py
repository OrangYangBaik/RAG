import os

LOCAL_LLM_API = {
    "base_url": os.getenv("BASE_URL"),
    "api_key": os.getenv("API_KEY"),
    "model_LLM": os.getenv("MODEL_LLM"),
    "model_embed": os.getenv("MODEL_EMBED")
}
