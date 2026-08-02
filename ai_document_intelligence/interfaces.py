from __future__ import annotations

from typing import Protocol

from .models import ParsedDocument


class DocumentParser(Protocol):
    """Protocol for document parsing implementations."""

    def parse(self, source: str) -> ParsedDocument:
        ...
