"""
Simple UI: CLI-based
"""
from rag_chain import query_llm

if __name__ == "__main__":
    while True:
        q = input("Please ask questions (exit to finish):")
        if q.strip().lower() == "exit":
            break
        print("\nAnswer:")
        print(query_llm(q))