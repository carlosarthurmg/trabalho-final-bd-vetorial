import pdfplumber

def extract_text_from_pdf(path):
    texts = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            texts.append({"page": i, "text": text})
    return texts

def chunk_text(text, chunk_size_chars=1500, overlap=200):
    chunks = []
    start = 0
    length = len(text)
    if length == 0:
        return []
    while start < length:
        end = start + chunk_size_chars
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start = max(end - overlap, end)
    return chunks
