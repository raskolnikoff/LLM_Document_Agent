# ingest/parser.py
import os
import hashlib
import pickle
import unicodedata
from llm_parsers.parsers import parse_file

DOC_DIR = "docs"
CACHE_DIR = ".parsed_cache"
PARSED_OUTPUT = "store/parsed.pkl"

os.makedirs(CACHE_DIR, exist_ok=True)


# File name normalization function
def normalize_filename(name):
    return unicodedata.normalize("NFKC", name)


all_docs = []
for filename in os.listdir(DOC_DIR):
    norm_filename = normalize_filename(filename)
    filepath = os.path.join(DOC_DIR, norm_filename)

    if not os.path.isfile(filepath):
        continue

    try:
        with open(filepath, "rb") as f:
            content = f.read()
            doc_hash = hashlib.md5(content).hexdigest()

        hash_path = os.path.join(CACHE_DIR, norm_filename + ".md5")
        if os.path.exists(hash_path):
            with open(hash_path) as f:
                old_hash = f.read().strip()
            if old_hash == doc_hash:
                print(f"✅ Cached: {norm_filename}")
                continue

        print(f"📄 Parsing: {norm_filename}")
        doc = parse_file(filepath)
        all_docs.append(doc)

        with open(hash_path, "w") as f:
            f.write(doc_hash)

    except Exception as e:
        print(f"❌ Failed: {norm_filename} - {repr(e)}")

# Save parsed output only if new docs were added
if all_docs:
    with open(PARSED_OUTPUT, "wb") as f:
        pickle.dump(all_docs, f)
    print(f"✅ Saved parsed documents: {len(all_docs)}")
else:
    print("🔁 No new documents parsed.")
