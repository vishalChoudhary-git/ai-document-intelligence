from __future__ import annotations

from .exceptions import ParseError


def parse_document(source: str) -> dict[str, str]:
    """Parse a document source into a normalized document structure.

    This starter implementation validates the input and raises a domain-specific
    error if parsing is not possible.
    """
    if not source or not source.strip():
        raise ParseError("Document source must not be empty.")

    return {"source": source, "status": "parsed"}
