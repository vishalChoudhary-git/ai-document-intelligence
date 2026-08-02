from pydantic import BaseModel

from .document_metadata import DocumentMetadata
from .page import Page


class ParsedDocument(BaseModel):
    """Normalized parser output."""

    raw_text: str

    pages: list[Page]

    metadata: DocumentMetadata