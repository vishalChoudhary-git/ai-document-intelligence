import fitz

from ai_document_intelligence.models import (
    DocumentMetadata,
    Page,
    ParsedDocument,
)

from .base_parser import BaseParser


class PyMuPDFParser(BaseParser):

    def parse(
        self,
        content: bytes,
    ) -> ParsedDocument:

        pdf = fitz.open(
            stream=content,
            filetype="pdf",
        )

        pages = []

        raw_text = []

        for index, page in enumerate(pdf):

            text = page.get_text()

            raw_text.append(text)

            pages.append(
                Page(
                    number=index + 1,
                    text=text,
                )
            )

        metadata = pdf.metadata or {}

        document_metadata = DocumentMetadata(
            title=metadata.get("title"),
            author=metadata.get("author"),
            creator=metadata.get("creator"),
            producer=metadata.get("producer"),
            creation_date=metadata.get("creationDate"),
            modification_date=metadata.get("modDate"),
            page_count=len(pages),
        )

        pdf.close()

        return ParsedDocument(
            raw_text="\n".join(raw_text),
            pages=pages,
            metadata=document_metadata,
        )