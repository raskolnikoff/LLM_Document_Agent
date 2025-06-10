# 📚 LLM Document Agent

[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://llmdocumentagent-fvhqjfvw3vc6mhgrmhdkdw.streamlit.app/)

> The privacy-first, local-first AI assistant for your documents.
> Query, summarize, and reason across your PDF/EPUB library – all on your machine.

---

## 🚀 Features

- 🛡️ 100% offline document RAG (no data ever leaves your device)
- 📚 Supports PDF/EPUB and rapid semantic vector search
- 🤖 Local LLMs (Ollama, Llama3) or cloud/demo fallback (Streamlit Cloud)
- ⚡ Lightning-fast QA for massive knowledge libraries
- 🖥️ Beautiful UI with Streamlit ([Live Demo](https://llmdocumentagent-fvhqjfvw3vc6mhgrmhdkdw.streamlit.app/))
- 🛠️ Easy to extend, hack, and deploy on any OS

---

## 🌟 Try it in your browser

**[▶️ Live Streamlit Cloud Demo](https://llmdocumentagent-fvhqjfvw3vc6mhgrmhdkdw.streamlit.app/)**  
*(Note: Demo disables local LLMs for security. Run locally for full power!)*

---

## ❓ Why LLM Document Agent?

Most document Q&A tools require uploading your private files to third-party servers or depend on closed APIs.  
**LLM Document Agent** is fully open-source, 100% offline-ready, and gives you back control over your knowledge and data.

---

## 📦 Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/raskolnikoff/LLM_Document_Agent.git
cd LLM_Document_Agent

# 2. Install requirements
pip install -r requirements.txt

# 3. Add your PDF/EPUB files into docs/
# 4. Run the pipeline (to parse/index your files)
python app/parser.py
python app/chunk_embed.py

# 5. Start the UI
streamlit run app/web_ui.py
```

---

## 🗂️ Directory Structure (flat app/ example)

```
LLM_Document_Agent/
├── app/
│   ├── web_ui.py
│   ├── rag_chain.py
│   ├── indexer.py
│   ├── ...
├── docs/
│   └── your-books.pdf
├── index.faiss
├── metadatas.pkl
├── requirements.txt
├── README.md
```

---

## 🛠️ FAQ / Troubleshooting

**Q. Why doesn't local LLM (Ollama) work on Streamlit Cloud?**  
A. Cloud demos cannot run system-level LLMs for security; run locally for full features!

**Q. I updated my docs – how do I refresh the index?**  
A. Re-run the parser and embedder steps (`python app/parser.py && python app/chunk_embed.py`).

**Q. Can I use with other LLM APIs (OpenAI, Anthropic)?**  
A. Easily hackable – add your API calls to `rag_chain.py`.

---

## 📖 License

MIT License

---

> Built with ❤️ in Japan.  
> OSS contributions, feature requests, and issues welcome!
