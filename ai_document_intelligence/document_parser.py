from pathlib import Path

from .models import ParsedDocument
from .parsers.pymupdf_parser import PyMuPDFParser


class DocumentParser:

    def __init__(self) -> None:

        self._parser = PyMuPDFParser()

    def parse(
        self,
        content: bytes,
    ) -> ParsedDocument:

        return self._parser.parse(content)

    def parse_file(
        self,
        file_path: str | Path,
    ) -> ParsedDocument:

        with open(file_path, "rb") as file:

            return self.parse(file.read())