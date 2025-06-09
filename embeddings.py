from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def get_embeddings(chunks):
    return model.encode(chunks)


def embed_query(query):
    return model.encode([query])[0]