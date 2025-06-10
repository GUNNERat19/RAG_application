# from sentence_transformers import SentenceTransformer
# from config import EMBEDDING_MODEL

# model = SentenceTransformer(EMBEDDING_MODEL)

# def get_embeddings(chunks):
#     return model.encode(chunks)


# def embed_query(query):
#     return model.encode([query])[0]


import requests

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL_EMB = "mxbai-embed-large"  # Ollama embedding model

def get_embeddings(chunks):
    return [embed_query(chunk) for chunk in chunks]

def embed_query(text):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json={"model": OLLAMA_MODEL_EMB, "prompt": text}
    )
    response.raise_for_status()
    return response.json()["embedding"]