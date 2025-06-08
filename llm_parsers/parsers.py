# llm_parsers/parsers.py
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from unstructured.partition.pdf import partition_pdf
from unstructured.documents.elements import NarrativeText
import os


def extract_epub_text(epub_path):
    book = epub.read_epub(epub_path)
    texts = []
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            texts.append(soup.get_text())
    return '\n'.join(texts)


def parse_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        elements = partition_pdf(filename=filepath, strategy="fast")
        return {"path": filepath, "elements": elements}

    elif ext == ".epub":
        text = extract_epub_text(filepath)
        paragraphs = [para.strip() for para in text.split("\n") if para.strip()]
        elements = [NarrativeText(text=para) for para in paragraphs]
        return {"path": filepath, "elements": elements}

    else:
        raise ValueError(f"Unsupported file format: {filepath}")
