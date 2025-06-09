import sys
from rag_pipeline import ingest, ask

if __name__ == "__main__":
    if sys.argv[1] == "ingest":
        ingest(sys.argv[2])  # Pass PDF path
    elif sys.argv[1] == "ask":
        response = ask(" ".join(sys.argv[2:]))
        print(response)