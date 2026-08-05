# AI Document Intelligence

A Python SDK for document intelligence, PDF parsing, and structured extraction for LLM and RAG applications.

## Features

- 📄 Intelligent PDF parsing powered by PyMuPDF
- 📑 Page-wise text extraction
- 📋 Document metadata extraction
- 🧩 Unified parsing API
- ⚡ Supports multiple input sources (`str`, `Path`, `bytes`)
- 🐍 Typed models powered by Pydantic

## Installation

```bash
pip install ai-document-intelligence
```

## Quick Start

```python
from ai_document_intelligence import DocumentParser

parser = DocumentParser()

document = parser.parse("annual_report.pdf")

print(document.metadata.page_count)
print(document.pages[0].text)
```

## Supported Input Types

The parser exposes a single `parse()` method that accepts multiple input sources.

### Parse from a file path

```python
document = parser.parse("annual_report.pdf")
```

### Parse from a `Path`

```python
from pathlib import Path

document = parser.parse(Path("annual_report.pdf"))
```

### Parse from bytes

```python
from pathlib import Path

pdf_bytes = Path("annual_report.pdf").read_bytes()

document = parser.parse(pdf_bytes)
```

## Returned Object

```python
document.raw_text
document.pages
document.metadata
```

Example:

```python
print(document.metadata.title)
print(document.metadata.page_count)

for page in document.pages:
    print(page.number)
    print(page.text)
```

## Roadmap

### v0.1.0
- ✅ PDF parsing
- ✅ Page-wise text extraction
- ✅ Metadata extraction
- ✅ Unified parsing API (`parse()`)
- ✅ Support for `str`, `Path`, and `bytes`

### Upcoming

- 🚧 Docling backend
- 🚧 OCR support
- 🚧 Table extraction
- 🚧 Layout detection
- 🚧 Semantic chunking
- 🚧 Image extraction