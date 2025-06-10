# query/rag_chain.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

MODEL_NAME = "intfloat/multilingual-e5-base"
LLM_MODEL = "llama3"
USE_OLLAMA = os.environ.get("USE_OLLAMA", "1") == "1"

if USE_OLLAMA:
    try:
        import ollama
    except ImportError:
        ollama = None
else:
    ollama = None

with open("metadatas.pkl", "rb") as f:
    metadatas = pickle.load(f)

index = faiss.read_index("index.faiss")
embedder = SentenceTransformer(MODEL_NAME)


def query_llm(question, top_k=5, target_files=None):
    q_emb = embedder.encode([question])
    D, I = index.search(np.array(q_emb), top_k)
    filtered = []

    for i in I[0]:
        meta = metadatas[i]
        source_file = os.path.basename(meta["source"])
        if target_files is None or source_file in target_files:
            filtered.append((i, meta))

    context = "\n".join([
        f"From {m['source']}: chunk {i}" for i, m in filtered
    ])

    if ollama:
        # ローカルLLM (Ollama) の場合
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": question}])
        return response['message']['content'], []
    else:
        # Streamlit Cloud等、Ollama未使用時のダミー回答
        return (
            "Sorry, local LLM (Ollama) is not available on Streamlit Cloud.\n"
            "Try this app locally with Ollama for full functionality!", []
        )

    prompt = f"""
You are a helpful assistant. Only answer using the following context.
If you don't know, say "Not available in the provided documents."

Context:
{context}

Question: {question}
Answer:
"""

    response = ollama.chat(model=LLM_MODEL, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'], [
        {"file": os.path.basename(m["source"]), "page": m.get("page", "?"), "content": "..."}
        for _, m in filtered
    ]
