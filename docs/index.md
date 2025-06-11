# 📚 LLM Document Agent

[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://llmdocumentagent-j7vpndghp2wayqvnfeo2ac.streamlit.app/)

> The privacy-first, open-source, local-first AI assistant for your documents.
> Query, summarize, and reason across your PDF/EPUB library — all on your machine.

---

### 🚀 Features

* 🛡️ 100% offline document RAG (private, no cloud upload needed)
* 📚 Supports both PDF & EPUB, with fast semantic vector search
* 🤖 Local LLM support (Ollama, Llama3) — fallback to demo mode in Cloud
* ⚡ Lightning-fast QA for massive libraries
* 🖥️ Modern, responsive UI (Streamlit)
* 🌍 Ready for OSS collaboration, extensible/hackable codebase
* 🔗 [Live Demo](https://llmdocumentagent-j7vpndghp2wayqvnfeo2ac.streamlit.app/) using public domain books

---

### 🌟 Try it instantly (no install)

**[▶️ Try Live Demo on Streamlit Cloud](https://llmdocumentagent-j7vpndghp2wayqvnfeo2ac.streamlit.app/)**
*(Demo includes pre-indexed public domain books from [Project Gutenberg](https://www.gutenberg.org/). Local LLMs are disabled for security. Try locally for full power!)*

---

### 📖 What makes LLM Document Agent different?

Most doc Q\&A tools force you to upload private data to the cloud, or lock you into a closed AI API.
**LLM Document Agent** is 100% offline, open-source, and puts *you* in control — your files, your server, your AI.

---

### 📦 Quick Start (Local Use)

```bash
# 1. Clone the repo
git clone https://github.com/raskolnikoff/LLM_Document_Agent.git
cd LLM_Document_Agent

# 2. Install requirements (Python 3.9+ recommended)
pip install -r requirements.txt

# 3. Add your PDF/EPUB files to docs/
#    Or keep the sample public domain files for testing

# 4. Build your vector index
python app/parser.py
python app/chunk_embed.py

# 5. Launch the web UI
streamlit run app/web_ui.py

# 6. (Optional) To use Ollama/LLM locally, start Ollama server:
ollama serve &
```

---

### 🗂️ Directory Structure

```
LLM_Document_Agent/
├── app/
│   ├── web_ui.py
│   ├── rag_chain.py
│   ├── indexer.py
│   └── ...
├── docs/
│   ├── frankenstein.epub
│   ├── pride_and_prejudice.epub
│   └── ... (other demo/public books)
├── index.faiss
├── metadatas.pkl
├── requirements.txt
├── README.md
├── run_pipeline.sh
└── .gitignore
```

* `docs/` ... Place your PDFs/EPUBs here (demo branch includes public domain books)
* `index.faiss`, `metadatas.pkl` ... Prebuilt vector index and metadata (auto-generated, included for demo)

---

### 🌍 About the Demo

This repo includes a “demo” branch preloaded with [Project Gutenberg](https://www.gutenberg.org/) public domain books (no copyright restrictions).
**You can try the web app instantly on Streamlit Cloud, with no setup — just open [the demo link](https://llmdocumentagent-j7vpndghp2wayqvnfeo2ac.streamlit.app/)!**

* All demo books are legal to redistribute and analyze for OSS/AI purposes.
* For your private docs, use the “main” branch locally for full privacy & LLM power.

---

### 🛠️ FAQ / Troubleshooting

**Q. Why doesn't Ollama/LLM work in the Cloud demo?**
A. For security reasons, Streamlit Cloud disables local LLMs and external server calls.
　→ Use local mode for full-power QA and private data analysis.

**Q. I added/removed docs — how to refresh the search?**
A. Run `python app/parser.py && python app/chunk_embed.py` to rebuild the index.

**Q. I want to add OpenAI/Anthropic or other LLMs!**
A. Codebase is modular — add your API logic in `app/rag_chain.py`.

**Q. Error: No documents to select / nothing appears?**
A. Confirm you have at least one valid `.pdf` or `.epub` in `docs/`, and that you rebuilt the index.

---

### 🤝 Contributing

Pull requests, issues, and ideas are super welcome!
Let’s make privacy-first document AI accessible to all.

---

### 📖 License

MIT License

> Built with ❤️ in Japan.
> OSS contributions, feature requests, and issues welcome!
