# query/rag_chain.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

MODEL_NAME = "intfloat/multilingual-e5-base"
LLM_MODEL = "llama3"
LLM_BACKEND = os.environ.get("LLM_BACKEND", "ollama")  # "ollama" or "dummy" (for Cloud)


# ---- LLM Backend 抽象クラス実装 ----

class LLMBackend:
    def __init__(self, backend=LLM_BACKEND, model_name=LLM_MODEL):
        self.backend = backend
        self.model_name = model_name

        if backend == "ollama":
            try:
                import ollama
                self.ollama = ollama
            except ImportError:
                self.ollama = None
        else:
            self.ollama = None

    def query(self, prompt, context=None):
        # context（RAG context）は今後の拡張用
        if self.backend == "ollama" and self.ollama:
            # 必要に応じてcontextをpromptに加える
            # prompt = f"{context}\n\n{prompt}" ←後でカスタマイズOK
            response = self.ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response['message']['content']
        elif self.backend == "dummy":
            return (
                "Sorry, local LLM (Ollama) is not available on Streamlit Cloud.\n"
                "Try this app locally with Ollama for full functionality!"
            )
        else:
            return "Backend not implemented!"


# ---- 既存処理 ----

with open("metadatas.pkl", "rb") as f:
    metadatas = pickle.load(f)

index = faiss.read_index("index.faiss")
embedder = SentenceTransformer(MODEL_NAME)

llm = LLMBackend()  # デフォルトはollama, Cloudは "dummy"


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

    # --- プロンプト設計：今後context拡張も容易にできる形 ---
    prompt = f"""
You are an expert assistant. Use only the provided context to answer the user's question.
If you don't know, say "Not available in the provided documents."

Your answer must be detailed, include explanations, reasoning, and refer to evidence or page numbers if available.
If relevant, summarize or paraphrase longer sections.

Context:
{context}

Question: {question}
Answer:
"""

    answer = llm.query(prompt)

    # --- 引用chunkリストも返す設計 ---
    sources = [
        {"file": os.path.basename(m["source"]), "page": m.get("page", "?"), "content": "..."}
        for _, m in filtered
    ]
    return answer, sources
