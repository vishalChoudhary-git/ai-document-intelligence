from pydantic import BaseModel

from .document_metadata import DocumentMetadata
from .page import Page


class ParsedDocument(BaseModel):

    raw_text: str

    pages: list[Page]

    metadata: DocumentMetadata