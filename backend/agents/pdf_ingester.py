import PyPDF2
import re
import os

def ingest_pdf(file_path):
    text_content = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text()
            cleaned = re.sub(r'\s+', ' ', text).strip()
            text_content.append({
                "page": page_num + 1,
                "content": cleaned
            })
    return text_content
