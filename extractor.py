#This program extracts paragraphs from the user file
import os
from pypdf import PdfReader
from docx import Document

def split_into_paragraphs(document):
    paragraphs = document["text"].splitlines()
    result = []
    for p in paragraphs:
        if p.strip():
            result.append({
                "text": p.strip(),
                "source": document["source"]
            })
    return result


def extract_text(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        txt = f.read()
    return {
        "text": txt,
        "page": 1,
        "source": os.path.basename(file_path)
    }

def extract_pdf(file_path):
    reader = PdfReader(file_path)
    pages = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text and len(text.split()) > 50:
            pages.append({
                "text": text,
                "page": page_num,
                "source": os.path.basename(file_path)
            })
    return pages

def extract_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return [
        {
            "text": text,
            "page": 1,
            "source": os.path.basename(file_path)
        }
    ]

#test start . Use if __name__ == "__main__": if commentin before test case commenting out this test case permanently
#if __name__ == "__main__":
  #  pdf = extract_pdf("data/sample.pdf")
  #  print("Pages extracted:", len(pdf))
  #  for page in pdf[:5]:
  #      print("\nSource:", page["source"])
  #      print("Page:", page["page"])
  #      print("Preview:", page["text"][:100])
if __name__ == "__main__":
    doc = extract_docx("data/sample.docx")
    print(doc)