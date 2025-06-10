# llm_utils/indexer.py
# Utility functions to manage document index and metadata

import os
import pickle

def load_metadatas(metadata_path="metadatas.pkl"):
    """
    Load metadata from pickle file.
    """
    if not os.path.exists(metadata_path):
        return []
    with open(metadata_path, "rb") as f:
        return pickle.load(f)

def get_available_files(parsed_cache_dir=".parsed_cache"):
    """
    Get list of files that have been successfully parsed and cached.
    """
    if not os.path.exists(parsed_cache_dir):
        return []

    filenames = []
    for f in os.listdir(parsed_cache_dir):
        if f.endswith(".md5"):
            safe_name = f.replace(".md5", "")
            filenames.append(safe_name)
    return sorted(filenames)
