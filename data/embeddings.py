from sentence_transformers import SentenceTransformer
import chromadb
from data.documents import documents

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_collection():
    client = chromadb.Client()
    collection = client.create_collection(name="ecommerce")

    texts = [doc["text"] for doc in documents]
    embeddings = model.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[doc["id"] for doc in documents],
        metadatas=[{"topic": doc["topic"]} for doc in documents]
    )

    return collection, model