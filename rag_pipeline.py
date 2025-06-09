from loader import extract_text_from_pdf, chunk_text
from embeddings import get_embeddings, embed_query
from retriever import store_chunks, query_chunks
from ollama_runner import query_ollama
from config import CHUNK_SIZE, CHUNK_OVERLAP

def ingest(file_path):
    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text, CHUNK_SIZE, CHUNK_OVERLAP)
    embeddings = get_embeddings(chunks)
    store_chunks(chunks, embeddings)


def ask(query):
    query_emb = embed_query(query)
    results = query_chunks(query_emb)
    if not results["documents"] or not results["documents"][0]:
        return "Sorry, I don't have enough information to answer that."

    context = "\n\n".join(results["documents"][0])
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.
If the context doesn't help, say you don't know.

Context:
{context}

Question:
{query}
"""
    return query_ollama(prompt)