from ai_document_intelligence.models import (
    DocumentMetadata,
    Page,
    ParsedDocument,
)


def test_parsed_document_model():

    document = ParsedDocument(
        raw_text="Hello",
        pages=[
            Page(
                number=1,
                text="Hello",
            )
        ],
        metadata=DocumentMetadata(
            page_count=1,
        ),
    )

    assert document.metadata.page_count == 1

    assert len(document.pages) == 1

    assert document.raw_text == "Hello"