import subprocess
from config import OLLAMA_MODEL

def query_ollama(prompt):
    result = subprocess.run(["ollama", "run", OLLAMA_MODEL], input=prompt.encode(), capture_output=True)
    return result.stdout.decode()