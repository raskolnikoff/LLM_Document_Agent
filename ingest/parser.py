# parser.py
"""
文書読み込み（PDF, Word, 画像、テキスト）
"""
import os
from unstructured.partition.pdf import partition_pdf

def load_documents(directory):
    docs = []
    print(f"📁 Scanning: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.lower().endswith(".pdf"):
                continue  # PDFのみ対象
            path = os.path.join(root, file)
            print(f"📄 Parsing: {path}")
            try:
                elements = partition_pdf(filename=path, strategy="fast")
                print(f"✅ Parsed: {len(elements)} elements from {path}")
                docs.append({"path": path, "elements": elements})
            except Exception as e:
                print(f"❌ Failed: {path} - {e}")
    return docs

if __name__ == "__main__":
    docs = load_documents("docs")
    print(f"📊 Total loaded: {len(docs)}")
