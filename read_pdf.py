from pypdf import PdfReader

pdf = PdfReader("documents\GenAI_Rag_guide.pdf")

for page in pdf.pages:
    text = page.extract_text()
    print(text)
