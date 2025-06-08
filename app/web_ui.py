import streamlit as st
from llm_parsers.parsers import parse_file
from query.rag_chain import query_llm

st.set_page_config(page_title="📚 Local LLM Document Agent", layout="wide")
st.title("📚 Local LLM Document Agent")

st.markdown("""
このアプリは、ローカルに保存されたPDF/EPUBを読み込み、ベクトル検索とローカルLLMを用いて自然言語での質問応答を実現します。
""")

uploaded_file = st.file_uploader("📤 ドキュメントをアップロード (PDF/EPUB)", type=["pdf", "epub"])

if uploaded_file is not None:
    st.success(f"アップロード完了: {uploaded_file.name}")
    st.write("📖 内容の読み取りとインデックス作成中...")
    parse_result = parse_file(uploaded_file)
    if parse_result:
        st.success("✅ ドキュメント処理完了")
    else:
        st.error("❌ ドキュメントの処理に失敗しました")

st.markdown("---")

query_text = st.text_input("💬 質問をどうぞ：")
if query_text:
    with st.spinner("💭 応答生成中..."):
        answer = query_llm(query_text)
        st.write("### ✨ 回答")
        st.write(answer)
