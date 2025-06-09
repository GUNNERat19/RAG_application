import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection("rag_data")

def store_chunks(chunks, embeddings):
    collection.add(documents=chunks, embeddings=embeddings, ids=[str(i) for i in range(len(chunks))])

def query_chunks(query_emb, k=5):
    return collection.query(query_embeddings=[query_emb], n_results=k)