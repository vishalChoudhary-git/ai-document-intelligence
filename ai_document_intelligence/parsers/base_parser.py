from abc import ABC, abstractmethod

from ai_document_intelligence.models import ParsedDocument


class BaseParser(ABC):

    @abstractmethod
    def parse(
        self,
        content: bytes,
    ) -> ParsedDocument:
        ...