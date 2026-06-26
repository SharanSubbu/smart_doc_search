import tempfile
import os
import streamlit as st
from extractor import extract_pdf,extract_text,extract_docx,split_into_paragraphs
from search import search_paragraph

st.title("Smart Document Search")
uploaded=st.file_uploader(
    "Upload document",
    type=["pdf","txt","docx"]
)

if uploaded:
    original_name=uploaded.name
    ext=os.path.splitext(original_name)[1].lower()
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=ext
    ) as tmp:
        tmp.write(uploaded.read())
        file_path=tmp.name
    if ext==".pdf":
        documents=extract_pdf(file_path)
        for d in documents:
            d["source"]=original_name
    elif ext==".txt":
        extracted=extract_text(file_path)
        extracted["source"]=original_name
        documents=split_into_paragraphs(extracted)
    elif ext==".docx":
        extracted=extract_docx(file_path)
        if isinstance(extracted,list):
            documents=[]
            for d in extracted:
                d["source"]=original_name
                documents.extend(split_into_paragraphs(d))
        else:
            extracted["source"]=original_name
            documents=split_into_paragraphs(extracted)
    st.write("Documents extracted:",len(documents))
    keyword=st.text_input("Search term")
    if keyword:
        results=search_paragraph(documents, keyword)
        if results:
            st.success(f"{len(results)} results found")
            for r in results:
                page=r.get("page",1)
                with st.expander(f"Page {page}"):
                    st.write(r["text"])
        else:
            st.warning("No results found")