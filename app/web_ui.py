import streamlit as st
from llm_parsers.parsers import parse_file
from query.rag_chain import query_llm

st.set_page_config(page_title="📚 Local LLM Document Agent", layout="wide")
st.title("📚 Local LLM Document Agent")

st.markdown("""
This app reads PDF/EPUB files saved locally and uses vector search and local LLM to enable natural language question-answering.
""")

uploaded_file = st.file_uploader("📤 Upload document (PDF/EPUB)", type=["pdf", "epub"])

if uploaded_file is not None:
    st.success(f"Upload complete: {uploaded_file.name}")
    st.write("📖 Reading content and creating index...")
    parse_result = parse_file(uploaded_file)
    if parse_result:
        st.success("✅ Document processing complete")
    else:
        st.error("❌ Failed to process document")

st.markdown("---")

query_text = st.text_input("💬 Please ask questions:")
if query_text:
    with st.spinner("💭 Generating response..."):
        answer = query_llm(query_text)
        st.write("### ✨ Answer")
        st.write(answer)
