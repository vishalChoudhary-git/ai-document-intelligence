from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DocumentMetadata:
    """Metadata container for parsed documents."""

    source: str | None = None
    title: str | None = None
    author: str | None = None
    creator: str | None = None
    producer: str | None = None
    creation_date: str | None = None
    modification_date: str | None = None
    page_count: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)
