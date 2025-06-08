# ingest/epub_parser.py
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

def extract_epub_text(epub_path):
    book = epub.read_epub(epub_path)
    texts = []
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            texts.append(soup.get_text())
    return '\n'.join(texts)
