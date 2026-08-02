from ai_document_intelligence.models import (
    DocumentMetadata,
    Page,
    ParsedDocument,
)


def test_parsed_document():

    document = ParsedDocument(
        raw_text="Hello World",
        pages=[
            Page(
                number=1,
                text="Hello World",
            )
        ],
        metadata=DocumentMetadata(
            page_count=1,
        ),
    )

    assert document.raw_text == "Hello World"
    assert document.metadata.page_count == 1
    assert document.pages[0].number == 1