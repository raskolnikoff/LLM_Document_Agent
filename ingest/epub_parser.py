import os
from unstructured.partition.pdf import partition_pdf

def load_documents(directory):
    docs = []
    print(f"📁 Searching in: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            print(f"📄 Trying to load: {path}")
            try:
                elements = partition_pdf(filename=path, strategy="fast")  # or "hi_res"
                print(f"✅ Parsed: {path} -> {len(elements)} elements")
                docs.append({"path": path, "elements": elements})
            except Exception as e:
                print(f"❌ Failed to parse {path}: {e}")
    return docs

if __name__ == "__main__":
    docs = load_documents("docs")
    print(f"\n📊 Total loaded documents: {len(docs)}")
