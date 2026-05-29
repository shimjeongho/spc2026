from langchain_community.document_loaders import TextLoader

loader = TextLoader("./hbm.txt", encoding="utf-8")
documents = loader.load()

print(f"불러온 문서의 갯수: {len(documents)}")

doc = documents[0]
print(f"page_content (앞 100글자):\n{doc.page_content[:100]}...\n")
print(f"metadata: {doc.metadata}")

"""
불러온 문서의 갯수: 1
page_content (앞 100글자):
High Bandwidth Memory (HBM)
고대역폭 메모리

메모리 반도체의 일종.

2013년 대한민국의 반도체 제조 기업 SK하이닉스가 세계 최초로 개발한 반도체 제품이...

metadata: {'source': './hbm.txt'}
"""