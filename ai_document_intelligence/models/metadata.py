from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Metadata:
    """Container for document metadata."""

    source: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)
