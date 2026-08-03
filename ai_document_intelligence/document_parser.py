from ai_document_intelligence.models import ParsedDocument
from ai_document_intelligence.parsers import PyMuPDFParser
from ai_document_intelligence.types import DocumentSource
from ai_document_intelligence.utils.document_loader import (
    DocumentLoader,
)


class DocumentParser:

    def __init__(self) -> None:

        self._parser: PyMuPDFParser = PyMuPDFParser()

    def parse(
        self,
        source: DocumentSource,
    ) -> ParsedDocument:

        content = DocumentLoader.load(source)

        return self._parser.parse(content)