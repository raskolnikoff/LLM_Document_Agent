# ✅ Feature: Streamlit UI Improvements for Better UX
# Includes: Loading Indicator, File Selection, Source Chunk Display
import sys
import os

os.environ["PYTHONPATH"] = "."

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from indexer import load_metadatas, get_available_files
from rag_chain import query_llm

st.set_page_config(page_title="Document QA Agent", layout="centered")
st.title("📚 Ask Questions to Your Documents")

import subprocess

# ファイルアップロード機能
st.sidebar.title("Document Management")
uploaded_file = st.sidebar.file_uploader("Upload PDF, EPUB, or TXT", type=["pdf", "epub", "txt"])

if uploaded_file is not None:
    save_dir = "docs"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"Uploaded: {uploaded_file.name}")

    # ここでパース&インデックス再構築
    with st.spinner("Indexing new document(s)..."):
        env = os.environ.copy()
        env["PYTHONPATH"] = "."
        subprocess.run(["python", "ingest/parser.py"], check=True, env=env)
        subprocess.run(["python", "ingest/chunk_embed.py"], check=True, env=env)
    st.sidebar.success("Indexing complete! You can now se six monthsarch this document.")

# --- 以降は既存のRAG検索UI/質問部分 ---
st.title("LLM Document Agent")

# --- File Selection Sidebar ---
st.sidebar.header("📁 Document Settings")
file_choices = get_available_files()
selected_files = st.sidebar.multiselect("Select documents to search in:", file_choices, default=file_choices)

if not selected_files:
    st.warning("Please select at least one document to search.")
    st.stop()

# --- Question Input ---
question = st.text_input("🔍 Ask your question:")

# --- Loading State ---
if question:
    with st.spinner("Thinking..."):
        answer, sources = query_llm(question, target_files=selected_files)

        st.markdown("### 🧠 Answer")
        st.write(answer)

        if sources:
            st.markdown("### 📖 Sources")
            for src in sources:
                st.markdown(f"- *{src['file']}*, page {src['page']}: {src['content']}")
