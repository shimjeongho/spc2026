import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./chroma_db"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def build_document(file_path, collection):
    store = Chroma(collection_name= collection, embedding_function=embeddings, persist_directory=DB_DIR)
    if store._collection.count() > 0:  # 지금은 단순 DB라서, 최초 1회만 빌드
        return store
    
    docs = TextLoader(file_path, encoding="utf-8").load()
    chunks = splitter.split_documents(docs)
    for c in chunks:
        c.metadata["source"] = os.path.basename(file_path)

    return Chroma.from_documents(chunks, embeddings, collection_name=collection, persist_directory=DB_DIR)

# 1. 컬렉션 두개 준비
collections = {
    "nvme": build_document("./nvme.txt", "nvme"),
    "hbm": build_document("./hbm.txt", "hbm"),
}
for name, store in collections.items():
    print(f"컬렉션: {name}, 청크개수: {store._collection.count()}")

# 2. 컬랙션 내 검색
def search_in(name, query, k=2):
    return collections[name].similarity_search(query, k=k)

def search_all(query, k_per=2):
    results = []
    for name, store in collections.items():
        for doc in store.similarity_search(query, k=k_per):
            doc.metadata["collection"] = name  # 어느 컬랙션에서 가져왔는지 기록
            results.append(doc)
    return results

query = "PCIe 인터페이스 속도는?"

print("\n질문: ", query)
print("\n=== 'nvme' 컬렉션에서 검색 ===")
for doc in search_in("nvme", query):
    # print(f" -> {doc.page_content[:100]}...")  # 내용이 길 수 있으니 앞부분만 출력
    print(f" -> {doc.page_content}")  

print("\n=== 'nvme', 'hbm' 등 있는 컬렉션에 이걸 다 검색 ===")
for doc in search_all(query):
    print(f" -> [{doc.metadata['collection']}] {doc.page_content}")

"""
컬렉션: nvme, 청크개수: 32
컬렉션: hbm, 청크개수: 53

=== 'nvme' 컬렉션에서 검색 ===
  - NVMe의 속도를 메모리 카드 업계에서도 주목했는지, NVMe를 접목한 새로운 SD 카드 규격이 발표되었다. #

PCI Express 3.0 세대에서는 단일 슬롯으로도 2~3 G...
  - 높은 대역폭 덕분에 플래시 메모리뿐만 아니라 차세대 비휘발성 램인 NVRAM의 인터페이스로도 사용되고 있다. 특이하게도 2가지의 풀네임이 있는데, 하나는 PCI Express에서 ...

(py312) C:\src\SPC2026\10.LangChain\7.RAG\3.store>python 1.multicollection.py
C:\src\SPC2026\10.LangChain\7.RAG\3.store\1.multicollection.py:5: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.
  from langchain_community.document_loaders import TextLoader
컬렉션: nvme, 청크개수: 32
컬렉션: hbm, 청크개수: 53

질문:  PCIe 인터페이스 속도는?

=== 'nvme' 컬렉션에서 검색 ===
 -> NVMe의 속도를 메모리 카드 업계에서도 주목했는지, NVMe를 접목한 새로운 SD 카드 규격이 발표되었다. #

PCI Express 3.0 세대에서는 단일 슬롯으로도 2~3 GB/s급, 4.0 발표 이후엔 단일 슬롯으로도 6~7 GB/s급 SSD들이 속속 등장하였고, 향후 더 높은 대역폭 규격의 버스가 나오고 컨트롤러가 발전한다면 보다 높은 대역폭 달성이 가능할 것으로 보인다. 현재 PCI Express 5.0에 대응할수 있는 SSD 컨트롤러가 여러 개 개발된 상태로, 그 중에서 Phison PS5026-E26 컨트롤러의 스펙은 DDR4 및 LPDDR4 DRAM 탑재, 순차 읽기 12GB/s, 순차 쓰기 11GB/s, 랜덤 읽기 1,500K IOPS, 랜덤 쓰기 2,000K IOPS로 알려져있다.
 -> 높은 대역폭 덕분에 플래시 메모리뿐만 아니라 차세대 비휘발성 램인 NVRAM의 인터페이스로도 사용되고 있다. 특이하게도 2가지의 풀네임이 있는데, 하나는 PCI Express에서 따온 이름이고, 다른 하나는 HCI(Host Controller Interface)에서 따온 이름이다.

2020년대부터 고성능 하드디스크도 읽고 쓰는 속도가 500MB/s를 넘기 시작해 SATA 3의 최대 대역폭에 도달했기 때문에 NVMe가 서서히 도입되었다. NVMe 2.0부터 하드디스크 같은 전통적인 디스크 계열도 지원하기 시작했다. 사실 SATA 이전부터 고성능/서버프레임쪽으로는 이전부터 SAS(SCSI)계열로 진화했다.
2. 성능[편집]
최대 6 Gbps의 전송 속도를 가지는 SATA 3과 비교하면 PCI Express로 동작하므로 20Gbps 이상의 대역폭도 쉽게 구현한다.

=== 'nvme', 'hbm' 등 있는 컬렉션에 이걸 다 검색 ===
 -> [nvme] NVMe의 속도를 메모리 카드 업계에서도 주목했는지, NVMe를 접목한 새로운 SD 카드 규격이 발표되었다. #

PCI Express 3.0 세대에서는 단일 슬롯으로도 2~3 GB/s급, 4.0 발표 이후엔 단일 슬롯으로도 6~7 GB/s급 SSD들이 속속 등장하였고, 향후 더 높은 대역폭 규격의 버스가 나오고 컨트롤러가 발전한다면 보다 높은 대역폭 달성이 가능할 것으로 보인다. 현재 PCI Express 5.0에 대응할수 있는 SSD 컨트롤러가 여러 개 개발된 상태로, 그 중에서 Phison PS5026-E26 컨트롤러의 스펙은 DDR4 및 LPDDR4 DRAM 탑재, 순차 읽기 12GB/s, 순차 쓰기 11GB/s, 랜덤 읽기 1,500K IOPS, 랜덤 쓰기 2,000K IOPS로 알려져있다.
 -> [nvme] 높은 대역폭 덕분에 플래시 메모리뿐만 아니라 차세대 비휘발성 램인 NVRAM의 인터페이스로도 사용되고 있다. 특이하게도 2가지의 풀네임이 있는데, 하나는 PCI Express에서 따온 이름이고, 다른 하나는 HCI(Host Controller Interface)에서 따온 이름이다.

2020년대부터 고성능 하드디스크도 읽고 쓰는 속도가 500MB/s를 넘기 시작해 SATA 3의 최대 대역폭에 도달했기 때문에 NVMe가 서서히 도입되었다. NVMe 2.0부터 하드디스크 같은 전통적인 디스크 계열도 지원하기 시작했다. 사실 SATA 이전부터 고성능/서버프레임쪽으로는 이전부터 SAS(SCSI)계열로 진화했다.
2. 성능[편집]
최대 6 Gbps의 전송 속도를 가지는 SATA 3과 비교하면 PCI Express로 동작하므로 20Gbps 이상의 대역폭도 쉽게 구현한다.
 -> [hbm] 1Gbps
128GB/s
2018년
GDDR6
32
18Gbps
72GB/s
약 4.3배
HBM2
1024
2.4Gbps
307GB/s
2020년
GDDR6X
32
21Gbps
84GB/s
약 5.5배
HBM2e
1024
3.6Gbps
460GB/s
2022년
GDDR6X
32
24Gbps
96GB/s
약 8.5배
HBM3
1024
6.4Gbps
819GB/s
2024년
GDDR7
32
32Gbps
128GB/s
약 9.6배
HBM3e
1024
9.6Gbps
1.2TB/s
2025년
GDDR7
32
42.5Gbps
170GB/s
약 14.7배
HBM4
2048
10Gbps
2.5TB/s
7.2. 그래픽카드 제품별 대역폭[편집]
연도
제품명
구분
(용량)
칩 개수
(총 용량)
대역폭
2015년
AMD 라데온 R9 FURY X
HBM1(4Hi)
(1GB)
4개
(4GB)
512GB/s
2016년
엔비디아 P100
HBM2(4Hi)
(4GB)
4개
(16GB)
732GB/s
2017년
 -> [hbm] GDDR과 비교해 보면 근본적인 구조의 차이로 인해 대역폭 면에서 HBM이 월등하게 우수하다. 삼성은 스택당 최대 8-Hi, 최대 3.2 GT/s, 410 GB/s, 총 16 GB를 지원하는 플래시볼트 HBM2E를 2020년 2월에 양산할 수 있게 되었다. SK하이닉스도 스택당 최대 8-Hi, 최대 3.6 GT/s, 460 GB/s, 총 16 GB를 지원하는 HBM2E를 개발하여 2020년 7월 대량 생산에 돌입했다고 한다. 그리고 2020년 11월 16일, NVIDIA가 전송속도 3.2 Gbps, 대역폭 2 TB/s의 HBM2E로 업그레이드된 A100 80 GB 연산 카드를 발표했다.
3.3. 2023년 이전[편집]
"""
