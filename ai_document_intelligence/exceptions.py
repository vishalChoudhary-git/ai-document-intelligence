class DocumentIntelligenceError(Exception):
    """Base exception for package-level failures."""


class ParseError(DocumentIntelligenceError):
    """Raised when a document cannot be parsed."""


class UnsupportedFormatError(DocumentIntelligenceError):
    """Raised when a file format is unsupported."""
