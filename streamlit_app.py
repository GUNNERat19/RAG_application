import streamlit as st
from rag_pipeline import ingest, ask
import os

st.set_page_config(page_title="RAG with Ollama", layout="wide")
st.title("📄 Custom RAG App with Ollama")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    ingest(file_path)
    st.success("Document ingested and processed!")

query = st.text_input("Ask a question based on the uploaded document")
if st.button("Ask") and query:
    with st.spinner("Generating answer..."):
        response = ask(query)
        st.markdown(f"**Answer:** {response}")