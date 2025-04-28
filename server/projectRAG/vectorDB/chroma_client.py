import chromadb
from chromadb.config import Settings

def get_chroma_client():
    return chromadb.Client(Settings(persist_directory="./chroma_db"))

