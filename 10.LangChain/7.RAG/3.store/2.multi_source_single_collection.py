import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./chroma_db"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

FILES = [
    "./nvme.txt",
    "./hbm.txt",
    "./cisc2024.pdf"
]

def load_any_docs(path):
    # 확장자에 따라서 자동으로 로더를 선택함
    if path.lower().endswith(".pdf"):
        return PyPDFLoader(path).load()
    else:
        return TextLoader(path, encoding="utf-8").load()

def build_document():
    chunks = []
    for path in FILES:
        part = splitter.split_documents(load_any_docs(path))
        for c in part:
            c.metadata["source"] = os.path.basename(path)  # 통합된 컬렉션 내에서, 문서를 구분하기 위해서, 각각의 청크에 메타데이터를 넣음
        chunks += part

    return Chroma.from_documents(chunks, embeddings, collection_name="unified", persist_directory=DB_DIR)

# 있으면 로드, 없으면 생성
store = Chroma(collection_name="unified", embedding_function=embeddings, persist_directory=DB_DIR)
if store._collection.count() == 0:
   store = build_document()

print(f"컬렉션 이름: unified, 청크 통합 계수: {store._collection.count()}")

# 컬렉션 이름: unified, 청크 통합 계수: 89


# 쿼리
query = "저장장치 인터페이스 속도는?"
print("질문: ", query)
for d in store.similarity_search(query, k=2):
    print(f"\n---\n[{d.metadata.get('source')}] {d.page_content}")

query = "가장 값싸고 가성비 좋은 패스트푸드는?"
print("질문: ", query)
for d in store.similarity_search(query, k=2):
    print(f"\n---\n[{d.metadata.get('source')}] {d.page_content}")


# 특정 메타데이터를 기반으로만 필터링을 원하면?
results = store.similarity_search(query, k=2, filter={"source": "hbm.txt"})
for d in results:
    print(f"\n---\n{d.page_content}")

"""
질문:  저장장치 인터페이스 속도는?

---
[nvme.txt] AHCI가 개발되던 시절에는 HDD가 주류라 느릿느릿 회전하는 플래터를 큐잉할 정도의 성능만 가지고 있으면 됐었다. 달리 말하면 이 당시에는 사우스브릿지를 통해 ATA로 통신하는 것만으로도 충분한 속도였고, 현재의 하드디스크는 여전히 이론상 6 Gbps(750MB/s)[2]의 SATA 3 대역폭을 전부 사용하지 못한다. 즉 PCI Express에 보조기억장치를 직결하는 것은 리소스 낭비였다. SATA 버스 최고대역폭(속도) 자체가 하드디스크의 최고 I/O 속도보다 넘사벽으로 빨랐기 때문이었다. 그러나 반도체를 이용하여 플래터 회전 없이 고속으로 접근 가능한 SSD의 기술이 점진적으로 발달하여, SSD의 속도가 SATA/AHCI의 최고 대역폭보다 커지는 시점이 왔고, 이에 대응하기 위하여 2007년 IDF(Intel Developer Forum 인텔 개발자 포럼)에서 처음으로 이 프로토콜이 논의되었다. 2008년 4월 인텔에 의하여 초안이 작성되어 2011년에 1.0 최종 버전이

---
[nvme.txt] 높은 대역폭 덕분에 플래시 메모리뿐만 아니라 차세대 비휘발성 램인 NVRAM의 인터페이스로도 사용되고 있다. 특이하게도 2가지의 풀네임이 있는데, 하나는 PCI Express에서 따온 이름이고, 다른 하나는 HCI(Host Controller Interface)에서 따온 이름이다.

2020년대부터 고성능 하드디스크도 읽고 쓰는 속도가 500MB/s를 넘기 시작해 SATA 3의 최대 대역폭에 도달했기 때문에 NVMe가 서서히 도입되었다. NVMe 2.0부터 하드디스크 같은 전통적인 디스크 계열도 지원하기 시작했다. 사실 SATA 이전부터 고성능/서버프레임쪽으로는 이전부터 SAS(SCSI)계열로 진화했다.
2. 성능[편집]
최대 6 Gbps의 전송 속도를 가지는 SATA 3과 비교하면 PCI Express로 동작하므로 20Gbps 이상의 대역폭도 쉽게 구현한다.
질문:  가장 값싸고 가성비 좋은 패스트푸드는?

---
[nvme.txt] CFExpress
SD Express
SATA Express
SATA Express의 PCIe 채널을 사용한다. 최대 2레인을 사용 가능하며 디바이스 단자는 SFF-8639를 사용하나, SATA Express 표준이 인기를 얻지 못 하면서 호스트 쪽에 이 단자를 채택하는 경우는 과도기 제품을 제외하면 없고, 엔터프라이즈는 이미 SAS/SATA/NVME Tri-mode를 지원하는 SFF-8000 계열 단자로 넘어간 상태이다.
5. 호환성[편집]

---
[nvme.txt] [1] 단, PCIe Gen. 1,2,3,4들은 보통 하위 호환성이 가능하다. 업그레이드를 고려하면 유용한 전략을 세울수있다.
[2] 실제로는 약 590~600MB/s - 8/10비트 인코딩 때문. 출처
[3] 이때 당시 가정집에 일반적으로 보급된 SSD는 2.5인치 크기의 SATA3 방식 120~128GB급이 겨우 하나 둘 달려 나오고 있었고 조금 더 투자한 사람은 250~256GB수준이며 읽기속도는 많아야 550MB/s 쓰기는 300~400MB/s 수준이었지만 가격은 13~25만원 수준이었다.
[4] 스펙이 이렇게 차이나는건 당연히 먼저 언급된 폼팩터와 레인 그리고 가정용이 아닌 엔터프라이즈용이었기 때문이다. 그리고 당연하겠지만 가격도 상당했으며 그 값에 맞게 칩셋등도 고급이라 수명 또한 현존하는 최신 가정용 SSD보다도 수명이 길다.

---
6. 단점[편집]
비싼 가격
HBM의 가장 큰 단점은 바로 비싼 가격. B2B로만 납품되는 물건이라 정확한 가격에 대해서는 알려진 바가 없으나, TrendForce 기준 HBM3e 1GB당 가격이 약 16달러, HBM4 1GB당 가격이 약 20달러로 추정된다. 마이크론 임원에 따르면 엔비디아 B100에 들어가는 HBM3e 8단의 가격이 400 ~ 500달러 수준이라고 한다. 또한 SK하이닉스가 루빈 아키텍쳐 가속기에 들어갈 HBM4 12단 36GB 칩셋 가격을 500달러로 제시했는데#, HBM4 1개에 70만 원이라는 어마어마한 가격을 자랑한다. 향후 16단 이상의 고단으로 가게 되면 기술적 난도와 높은 용량으로 인해 훨씬 더 비싸질 것으로 예상된다.

---
기울임체는 출시 예상 제품.
HBMHBM
HBM
셀앤비 에스테틱  
셀앤비 에스테틱
m.store.naver.com/places/detail?id=574941148
선릉피지 모공 블랙헤드 트러블전문, 셀앤비 에스테틱, 네이버 플레이스 후기 확인.
공원뷰가 보이는 빙수 맛집
map.naver.com/p/entry/place/2006091465
확 트인 공원 전망을 감상하며 마지막 한 스푼까지 맛있는 빙수를 즐겨보세요
올댓뷰티아카데미 변희원
올댓뷰티아카데미 변희원
allthat-admission.co.kr
수강료 조회오시는 길방문상담예약
취업도 창업도 결국 같은 길, 지금 준비하지 않으면 내일은 더 늦습니다.
[1] DRAM 소자를 사용해서 아파트나 마천루를 만들어 놓은 게 HBM이라고 이해하면 충분하다. 실제로 전문가들이 많이 쓰는 비유.
"""