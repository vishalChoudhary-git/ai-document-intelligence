from ai_document_intelligence import DocumentParser

parser = DocumentParser()

document = parser.parse("sample.pdf")

print(document.metadata)

print(document.pages[0].text)