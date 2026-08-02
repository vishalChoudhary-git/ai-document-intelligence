from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    """Metadata extracted from a document."""

    title: str | None = Field(default=None)

    author: str | None = Field(default=None)

    creator: str | None = Field(default=None)

    producer: str | None = Field(default=None)

    creation_date: str | None = Field(default=None)

    modification_date: str | None = Field(default=None)

    page_count: int