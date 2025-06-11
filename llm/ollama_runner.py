"""
Ollama model startup confirmation and test execution
"""
import subprocess


def ensure_model(model="llama3"):
    result = subprocess.run(["ollama", "run", model], input="Hello", text=True, capture_output=True)
    return result.stdout
