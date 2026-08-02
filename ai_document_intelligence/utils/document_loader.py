from pathlib import Path

from ai_document_intelligence.types import DocumentSource


class DocumentLoader:

    @staticmethod
    def load(
        source: DocumentSource,
    ) -> bytes:

        if isinstance(source, bytes):
            return source

        if isinstance(source, str):
            return Path(source).read_bytes()

        if isinstance(source, Path):
            return source.read_bytes()

        raise TypeError(
            f"Unsupported source type: {type(source)}"
        )