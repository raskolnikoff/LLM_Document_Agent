"""
ベクトル検索とLLM応答
"""
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import ollama

MODEL_NAME = "intfloat/multilingual-e5-base"
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
You are a helpful assistant. Only answer using the following context.
If you don't know, say "Not available in the provided documents."

Context:
{context}

Question: {question}
Answer:
"""
    response = ollama.chat(model=LLM_MODEL, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']