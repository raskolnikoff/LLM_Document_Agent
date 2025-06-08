"""
簡易UI: CLIベース
"""
from query.rag_chain import query_llm

if __name__ == "__main__":
    while True:
        q = input("質問をどうぞ（exitで終了）: ")
        if q.strip().lower() == "exit":
            break
        print("\n回答:")
        print(query_llm(q))