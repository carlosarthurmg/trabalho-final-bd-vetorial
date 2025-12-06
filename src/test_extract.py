from utils import extract_text_from_pdf, chunk_text

pages = extract_text_from_pdf("docs/apostila.pdf")
total = 0

for p in pages:
    ch = chunk_text(p["text"])
    total += len(ch)
    print("Página", p["page"], "- chunks:", len(ch))

print("Total chunks:", total)
