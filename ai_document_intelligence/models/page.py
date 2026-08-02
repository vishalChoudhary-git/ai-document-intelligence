from pydantic import BaseModel


class Page(BaseModel):
    """Represents a single page within a parsed document."""

    number: int

    text: str