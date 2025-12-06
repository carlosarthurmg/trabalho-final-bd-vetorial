import os
from supabase import create_client
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE = os.getenv("SUPABASE_TABLE", "documents")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2")

def ingest_pdf(path):
    pdf = PdfReader(path)
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()

        if not text:
            continue

        embedding = model.encode(text).tolist()

        supabase.table(TABLE).insert({
            "content": text,
            "embedding": embedding
        }).execute()

        print(f"✔ Página {page_num+1} inserida!")

if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1]
    ingest_pdf(pdf_path)
