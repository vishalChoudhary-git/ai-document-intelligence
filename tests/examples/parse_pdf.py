from ai_document_intelligence import DocumentParser

parser = DocumentParser()

document = parser.parse("sample.pdf")

print("=" * 80)
print(document.metadata)
print("=" * 80)

print(document.pages[0].text)