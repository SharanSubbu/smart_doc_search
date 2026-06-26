#search function to find matching paragraphs
import re

def search_paragraph(paragraphs, keyword):
    result = []
    keyword = keyword.lower()
    for p in paragraphs:
        text = p["text"].lower()
        words = re.findall(r"\b[a-z0-9]+\b", text)
        for word in words:
            if word.rstrip("s") == keyword.rstrip("s"):
                result.append(p)
                break
    return result
# test case start. Use if __name__ == __main__: if commentin before test case commenting out this test case permanently
#paragraphs=["Python is easy","SQLite stores data","Streamlit builds UI"]
#keyword="Data"
#print(search_paragraph(paragraphs,keyword))