# FAISS vector값들을 저장하는 DB // GPU 기반으로 연산하는거에 최적

# Chroma 사용
# pip install chromadb
# pip install langchain-chroma

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./chroma_db"
COLLECTION_NAME = "coding"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def build_store():
    docs = TextLoader("./hbm.txt", encoding="utf-8").load()
    chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(docs)
    store = Chroma.from_documents(
        chunks, embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR
    )
    return store

def load_store():
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )
    print(f"기존 DB 로딩 성공 - {store._collection.count()} 청크 로딩됨")
    return store

if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
    store = load_store()
else:
    store = build_store()

results = store.similarity_search("HBM이란 무엇인가요?", k=2)
# results = store.similarity_search("HBM의 성능은 어떤가요?", k=3)
for i, d in enumerate(results, start=1):
    # 60줄 축약
    print(f" {i} -> {d.page_content[:60]}...")
    # 전체
    # print(f" {i} -> {d.page_content}...")

"""
### results = store.similarity_search("HBM이란 무엇인가요?", k=2)

 1 -> HMC보다 쉬운 구현 난이도
HBM은 프로세서의 바로 위로 적층하는 것은 불가능하여 완전한 원칩은 구현할 수...
 2 -> SK하이닉스, AMD, 엔비디아 등이 상업화를 위한 협력에 착수하여 2013년에 SK하이닉스에서 HBM을 개...
 3 -> HBM2
8 채널 × 128-bit × 8-Hi
8
1024-bit
1.2
1200 MHz
(2.4 Gbps...
"""
"""
### results = store.similarity_search("HBM의 성능은 어떤가요?", k=3)

기존 DB 로딩 성공 - 53 청크 로딩됨
 1 -> HMC보다 쉬운 구현 난이도
HBM은 프로세서의 바로 위로 적층하는 것은 불가능하여 완전한 원칩은 구현할 수...
 2 -> SK하이닉스, AMD, 엔비디아 등이 상업화를 위한 협력에 착수하여 2013년에 SK하이닉스에서 HBM을 개...
 3 -> HBM2
8 채널 × 128-bit × 8-Hi
8
1024-bit
1.2
1200 MHz
(2.4 Gbps...
"""

"""
RAG 흐름

문서 로드
↓
청크 분리
↓
임베딩 생성
↓
Vector DB 저장
↓
유사도 검색
↓
검색 결과를 LLM에 전달
↓
최종 답변 생성
"""