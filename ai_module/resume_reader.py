import pdfplumber

pdf_path = "sample_resume.pdf"

with pdfplumber.open(pdf_path) as pdf:
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

print(text)
