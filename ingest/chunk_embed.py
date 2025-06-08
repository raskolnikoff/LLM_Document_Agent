# ingest/chunk_embed.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

MODEL_NAME = "intfloat/multilingual-e5-base"


def split_and_embed(docs, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    embedder = SentenceTransformer(MODEL_NAME)
    texts, metadatas = [], []

    for doc in docs:
        text_blocks = [
            el.text.strip() for el in doc["elements"]
            if hasattr(el, "text") and isinstance(el.text, str) and el.text.strip()
        ]
        if not text_blocks:
            continue
        joined_text = "\n".join(text_blocks)
        chunks = splitter.split_text(joined_text)

        if not chunks:
            continue

        texts.extend(chunks)
        metadatas.extend([{"source": doc["path"]}] * len(chunks))

    if not texts:
        print("❗ No text chunks were created. Embedding skipped.")
        return

    embeddings = embedder.encode(texts, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    os.makedirs("store", exist_ok=True)
    faiss.write_index(index, "store/index.faiss")
    with open("store/metadatas.pkl", "wb") as f:
        pickle.dump(metadatas, f)

    print(f"✅ Saved index with {len(texts)} chunks.")


if __name__ == "__main__":
    from llm_parsers.parsers import parse_file
    import pickle

    if os.path.exists("store/parsed.pkl"):
        with open("store/parsed.pkl", "rb") as f:
            docs = pickle.load(f)
        print(f"📥 Loaded {len(docs)} parsed documents.")
        split_and_embed(docs)
        print("✅ Embedding completed and stored.")
    else:
        print("❗ No parsed documents found. Run parser.py first.")