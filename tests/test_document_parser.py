from pathlib import Path

from ai_document_intelligence import DocumentParser


def test_parse_pdf() -> None:
    parser = DocumentParser()

    document = parser.parse(
        Path("tests/resources/Resume.pdf")
    )

    assert document.metadata.page_count == 1
    assert len(document.pages) == 1
    assert len(document.raw_text) > 0