from ai_document_intelligence.parsers import PyMuPDFParser


def test_parser_creation():

    parser = PyMuPDFParser()

    assert parser is not None