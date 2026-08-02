# AI Document Intelligence

A production-ready Python SDK for intelligent PDF parsing for LLM applications.

## Installation

```bash
pip install ai-document-intelligence
```

## Usage

```python
from ai_document_intelligence import DocumentParser

parser = DocumentParser()

document = parser.parse_file("sample.pdf")

print(document.metadata.page_count)
```