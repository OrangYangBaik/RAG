from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from services.utils import custom_chunk
from services.embed_service import LocalNomicEmbeddings

def load_and_embed(collection):
    loader = TextLoader("testing_docs/product.txt")
    documents = loader.load()

    text = documents[0].page_content

    chunks = custom_chunk(text)

    langchain_chunks = [Document(page_content=chunk) for chunk in chunks]

    texts = [doc.page_content for doc in langchain_chunks]

    embedding = LocalNomicEmbeddings()
    vectors = embedding.embed_documents(texts)

    collection.add(documents=texts, embeddings=vectors, ids=[f"doc-{i}" for i in range(len(texts))])