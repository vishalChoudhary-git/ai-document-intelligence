from abc import ABC
from abc import abstractmethod

from ai_document_intelligence.models import ParsedDocument


class BaseParser(ABC):
    """Base interface for all document parsers."""

    @abstractmethod
    def parse(
        self,
        content: bytes,
    ) -> ParsedDocument:
        """Parse document bytes."""
        raise NotImplementedError