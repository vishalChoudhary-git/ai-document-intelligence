# AI Document Intelligence

A Python SDK for document intelligence, PDF parsing, and structured extraction for LLM and RAG applications.
## Installation

```bash
pip install ai-document-intelligence
```

## Usage

```python
from ai_document_intelligence import DocumentParser

parser = DocumentParser()

document = parser.parse("annual_report.pdf")

print(document.metadata.page_count)
print(document.pages[0].text)
```

## Current Features

- PDF Parsing
- PyMuPDF Backend
- Metadata Extraction
- Page-wise Text Extraction
- Raw Text Extraction

## Roadmap

- Docling
- OCR
- Tables
- Layout Detection
- Smart Chunking