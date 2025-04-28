import requests
from langchain.embeddings.base import Embeddings
from config.settings import LOCAL_LLM_API

class LocalNomicEmbeddings(Embeddings):
    def __init__(self, base_url= LOCAL_LLM_API["base_url"]):
        self.endpoint = base_url + "/embeddings"

    def embed_documents(self, texts):
        payload = {
            "input": texts,
               "model": LOCAL_LLM_API["model_embed"]
        }
        response = requests.post(self.endpoint, json=payload)
        response.raise_for_status()
        return [d["embedding"] for d in response.json()["data"]]

    def embed_query(self, text):
        payload = {
            "input": [text],
            "model": LOCAL_LLM_API["model_embed"]
        }
        response = requests.post(self.endpoint, json=payload)
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]
