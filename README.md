# 📚 Local LLM Document Agent

This project is a local Retrieval-Augmented Generation (RAG) system that allows users to query personal PDF/EPUB documents using a local Large Language Model (LLM). It integrates document parsing, vector embedding, FAISS indexing, and a CLI/Streamlit Web UI powered by Ollama + llama3.

---

## ⚙️ Prerequisites

- Python 3.9+ (recommended via [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- Ollama (to run local LLMs like `llama3`): [https://ollama.com](https://ollama.com)
- Git
- Virtual environment tool (conda or venv)
- macOS/Linux (tested), Windows WSL2 might work

---

## 📁 Project Structure

```
LLM_Document_Agent/
├── app/
│   ├── ui.py              # CLI interface
│   └── web_ui.py          # Streamlit Web UI
├── ingest/
│   ├── parser.py          # Parses and caches documents
│   └── chunk_embed.py     # Text splitting + embedding + FAISS index
├── query/
│   └── rag_chain.py       # Vector search + LLM chat interface
├── llm_parsers/
│   └── parsers.py         # .pdf/.epub parsing logic
├── store/                 # Stores index + metadata
├── docs/                  # Your documents (PDF, EPUB)
├── run_pipeline.sh        # Pipeline automation script
└── README.md
```

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone <your_repo_url>
cd LLM_Document_Agent
```

2. **Set up environment (conda)**

```bash
conda create -n llm-rag python=3.9 -y
conda activate llm-rag
```

3. **Install Python packages**

```bash
pip install -r requirements.txt
# If not available, install manually:
pip install streamlit faiss-cpu langchain sentence-transformers ebooklib beautifulsoup4 unstructured ollama
```

4. **Start Ollama server in background**

```bash
ollama serve &
ollama run llama3  # will download model if needed
```

---

## 🚀 Usage

### Full pipeline (parse + embed + UI)

```bash
./run_pipeline.sh --gui  # Streamlit UI
./run_pipeline.sh --cli  # Terminal-based CLI
```

### Upload documents
Place your `.pdf` or `.epub` files in the `docs/` directory.

### Ask questions
- Web UI: Type natural questions like "Summarize this book" or "What did Miyazaki do in 1979?"
- CLI: Same functionality via terminal

---

## 🧠 Features

- PDF & EPUB parsing with character-normalized filenames (NFKC-safe)
- Automatic caching to avoid redundant re-parsing and re-embedding
- SentenceTransformer embedding (`intfloat/multilingual-e5-base`)
- FAISS vector index + metadata persistence
- LLM queries via Ollama (`llama3`, switchable)
- Streamlit Web UI or CLI interface

---

## ✨ Planned Improvements

### Functional Enhancements
- ✅ Incremental FAISS index updates (avoid full reprocessing)
- ✅ Handle multilingual filenames safely (Unicode normalization)
- ✅ Display source chunks and citation in answers
- 🔲 Upload documents via Streamlit UI
- 🔲 Select which documents to include in search
- 🔲 Better session & scroll handling in Web UI
- 🔲 Prompt templates & chain-of-thought enhancement
- 🔲 Option to switch between Ollama local LLM and OpenAI models

### Codebase Architecture
- 🔲 Clean up `PYTHONPATH` issues via modular packaging (`src/` style layout)
- 🔲 Rename `utils` to avoid naming conflicts (`llm_parsers`, etc.)
- 🔲 Move all logs and caches to dedicated folders (`.cache/`, `logs/`)
- 🔲 Add basic `pytest` tests for parsing and querying flow
- 🔲 Dockerize the app for easier deployment

### Documentation & CI/CD
- 🔲 Add license file (MIT/Apache2.0)
- 🔲 Include usage examples, screenshots & animated GIF
- 🔲 GitHub Actions for test/lint checks on push
- 🔲 Add public demo via Streamlit Cloud (optional)

### Future Features
- 🔲 LangChain/LLamaIndex adapter layer for advanced agent behavior
- 🔲 Chunk overlap tuning and top-k selection in UI/config
- 🔲 Document-type icons or filters in UI

---

## 🧑‍💻 Author
Developed collaboratively with GPT-4o and driven by precision, performance, and the vision of AI-human creative collaboration.

> "I hate lies." — Project Owner
