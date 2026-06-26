# Smart Document Search

A simple document search web application built with Python and Streamlit.

Upload a PDF, TXT, or DOCX file and search for text inside the document. Matching results are shown with page information where available.

## Features

* Upload PDF files
* Upload TXT files
* Upload DOCX files
* Search document contents
* View matching results
* Show page numbers for PDFs
* Web interface using Streamlit

## Project Structure

```text
smart_doc_search/
│
├── streamlit_app.py
├── extractor.py
├── search.py
├── requirements.txt
├── data/
└── README.md
```

## Install

Clone the repository:

```bash
git clone <repository-url>
cd smart_doc_search
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Start the application:

```bash
python -m streamlit run streamlit_app.py
```

Open the local address shown in the terminal.

Example:

```text
http://localhost:8501
```

## Usage

1. Open the web app
2. Upload a PDF, TXT, or DOCX file
3. Enter a search term
4. View matching results

## Current Limitations

* Searches exact text matches
* PDF quality depends on extracted text
* One file at a time

## Future Improvements

* Multiple file upload
* Better result ranking
* Keyword highlighting
* Improved search relevance

## Tech Stack

* Python
* Streamlit
* PyPDF
* python-docx
