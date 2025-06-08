# chunk_embed.py
"""
チャンク処理と多言語埋め込み生成
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

def split_and_embed(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    embedder = SentenceTransformer(MODEL_NAME)
    texts, metadatas = [], []
    # text_blocks = [el.text for el in docs["elements"] if hasattr(el, "text") and el.text.strip()]

    for doc in docs:
        text_blocks = [el.text for el in doc["elements"] if hasattr(el, "text")]
        joined_text = "\n".join(text_blocks)
        chunks = splitter.split_text(joined_text)
        texts.extend(chunks)
        metadatas.extend([{"source": doc["path"]}] * len(chunks))

    embeddings = embedder.encode(texts, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    os.makedirs("store", exist_ok=True)
    faiss.write_index(index, "store/index.faiss")
    with open("store/metadatas.pkl", "wb") as f:
        pickle.dump(metadatas, f)

if __name__ == "__main__":
    from parser import load_documents
    docs = load_documents("docs")
    print(f"📥 Loaded {len(docs)} documents for embedding")
    split_and_embed(docs)
    print("✅ Embedding completed and stored.")
