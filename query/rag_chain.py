# rag_chain.py
"""
ベクトル検索とLLM応答
"""
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import ollama

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LLM_MODEL = "llama3"

with open("store/metadatas.pkl", "rb") as f:
    metadatas = pickle.load(f)

index = faiss.read_index("store/index.faiss")
embedder = SentenceTransformer(MODEL_NAME)

def query_llm(question, top_k=5):
    q_emb = embedder.encode([question])
    D, I = index.search(np.array(q_emb), top_k)
    context = "\n".join([f"From {metadatas[i]['source']}: {i}" for i in I[0]])
    prompt = f"""
You are a helpful assistant. Use the following context to answer:
{context}

Question: {question}
Answer:
"""
    response = ollama.chat(model=LLM_MODEL, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
