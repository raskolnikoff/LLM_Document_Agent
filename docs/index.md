# 📘 LLM Document Agent (Docs)

Welcome to the official documentation for **LLM Document Agent**, an offline-friendly, privacy-preserving RAG (Retrieval-Augmented Generation) system for answering deep questions from your own documents using LLMs.

## 🔍 What Is It?

**LLM Document Agent** lets you:

* Load your own PDF or EPUB files
* Parse and embed them using multilingual semantic models
* Search semantically relevant content from your knowledge
* Ask questions via a beautiful Streamlit interface

All locally. All privately.

## 🚀 Key Features

* 📁 Input formats: `.pdf`, `.epub`
* 📥 Parsing with cache & hash-based deduplication
* ✂️ Intelligent chunking with multilingual-e5 embedding
* ⚡ Fast vector search with FAISS
* 🤖 LLM-powered answers with Ollama + Llama3
* 🖥️ UI via Streamlit with file targeting and chunk citation
* 🧱 Clean modular architecture

## 💻 How to Use

1. 📂 Drop files into `docs/`
2. 🔧 Run the full pipeline:

   ```bash
   bash run_pipeline.sh
   ```
3. 🌐 Launch the UI:

   ```bash
   streamlit run app/web_ui.py
   ```

## ✨ Example Questions

* *"What is the central theme of Goethe’s Faust?"*
* *"How does Mary Shelley describe scientific ethics in Frankenstein?"*
* *"What is the role of time in Benjamin’s autobiographical fragments?"*

## 📸 Demo Preview

> A screenshot showing a sample question and AI-powered answer from a public domain text like *Frankenstein* or *Faust*.

*(📷 Insert image here)*

## 📚 Recommended Use Cases

* Personal knowledge bases
* Academic research
* Offline reading companions
* Secure organizational document Q\&A

## 🔐 Local-First Philosophy

This project is designed for:

* 🛡️ Privacy-first environments
* 🛠️ Local development
* 📚 Self-sovereign knowledge systems

## 🔗 More

* [GitHub Repository](https://github.com/raskolnikoff/LLM_Document_Agent)
* [Try the Live Demo (Streamlit Cloud)](https://share.streamlit.io/raskolnikoff/LLM_Document_Agent/main/app/web_ui.py)

---

> Built with ❤️ by open-source contributors who believe in local AI and accessible knowledge.
