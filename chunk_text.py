
from read_pdf import pdf

chunk_size = 1000
overlap = 200

chunks = []

for page_number, page in enumerate(pdf.pages, start=1):

    text = page.extract_text() or ""

    for i in range(0, len(text), chunk_size - overlap):

        chunk = text[i:i + chunk_size]

        chunks.append({
            "text": chunk,
            "page": page_number
        })

print("Total chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0]["text"])

print("\nPage number:", chunks[0]["page"])
