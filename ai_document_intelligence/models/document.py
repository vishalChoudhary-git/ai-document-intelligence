from pydantic import BaseModel


class DocumentMetadata(BaseModel):

    title: str | None = None

    author: str | None = None

    creator: str | None = None

    producer: str | None = None

    creation_date: str | None = None

    modification_date: str | None = None

    page_count: int