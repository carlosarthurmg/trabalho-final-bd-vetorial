import os
from supabase import create_client
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE = os.getenv("SUPABASE_TABLE", "documents")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2")

def search(query):
    query_vec = model.encode(query).tolist()

    response = supabase.rpc(
        "match_documents", 
        {"query_embedding": query_vec, "match_count": 5}
    ).execute()

    return response.data

def main():
    print("📘 Chat RAG rodando sem OpenAI!")

    while True:
        user = input("\nVocê: ")

        if user.lower() in ["sair", "exit", "quit"]:
            break

        try:
            results = search(user)

            if not results:
                print("Nenhum resultado encontrado.")
                continue

            print("\n🔍 Resultados relevantes:\n")
            for r in results:
                print("- ", r["content"][:300], "...\n")

        except Exception as e:
            print("Erro:", e)


if __name__ == "__main__":
    main()
