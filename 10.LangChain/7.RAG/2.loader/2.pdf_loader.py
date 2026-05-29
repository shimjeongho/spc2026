# pip install pypdf
# 이거 외에도 다양한 pdf 로더가 있음 fitz 라는 것도 유명함

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./Javascript_Secure_Coding.pdf")
pages = loader.load()

print(f"PDF 페이지수: {len(pages)}\n")

for p in pages:
    if p.page_content.strip():
        print(f"발견한 내용이 있는 첫페이지 metadata:\n{p.metadata}")
        print(f"페이지내용 (앞 400글자):\n{p.page_content[:400]}...")
        break
    """
    PDF 페이지수: 159

    발견한 내용이 있는 첫페이지 metadata:
    {'producer': 'Hancom PDF 1.3.0.546', 'creator': 'Hwp 2020 11.0.0.8362', 'creationdate': '2024-04-01T17:52:07+09:00', 'author': 'TEST', 'moddate': '2024-04-01T17:52:07+09:00', 'pdfversion': '1.4', 'source': './Javascript_Secure_Coding.pdf', 'total_pages': 159, 'page': 1, 'page_label': '2'}
    페이지내용 (앞 400글자):
    CONTENTS
    PART 제1장 개요제1절 배경····················································································2제2절 왜 자바스크립트인가··························································4제3절 가이드 목적 및 구성·························································6
    PART 제2장 시큐어코딩 가이드제1절 입력데이터 검증 및 표현················································101. SQL 삽입················································...
    """