# ✅ Feature: Streamlit UI Improvements for Better UX
# Includes: Loading Indicator, File Selection, Source Chunk Display

import streamlit as st
from .llm_utils.indexer import load_metadatas, get_available_files

from query.rag_chain import query_llm

st.set_page_config(page_title="Document QA Agent", layout="centered")
st.title("📚 Ask Questions to Your Documents")

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
