import fitz

from ai_document_intelligence.models import (
    DocumentMetadata,
    Page,
    ParsedDocument,
)

from .base_parser import BaseParser


class PyMuPDFParser(BaseParser):
    """PDF parser powered by PyMuPDF."""

    def parse(
        self,
        content: bytes,
    ) -> ParsedDocument:

        pdf = fitz.open(
            stream=content,
            filetype="pdf",
        )

        pages: list[Page] = []

        raw_text: list[str] = []

        metadata = pdf.metadata or {}

        try:

            for index, page in enumerate(pdf):

                text = page.get_text()

                raw_text.append(text)

                pages.append(
                    Page(
                        number=index + 1,
                        text=text,
                    )
                )

            return ParsedDocument(
                raw_text="\n".join(raw_text),
                pages=pages,
                metadata=DocumentMetadata(
                    title=metadata.get("title"),
                    author=metadata.get("author"),
                    creator=metadata.get("creator"),
                    producer=metadata.get("producer"),
                    creation_date=metadata.get("creationDate"),
                    modification_date=metadata.get("modDate"),
                    page_count=len(pages),
                ),
            )

        finally:

            pdf.close()