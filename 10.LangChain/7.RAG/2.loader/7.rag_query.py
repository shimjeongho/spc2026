# FAISS vector값들을 저장하는 DB // GPU 기반으로 연산하는거에 최적

# Chroma 사용
# pip install chromadb
# pip install langchain-chroma

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./chroma_db"
COLLECTION_NAME = "coding"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def build_store():
    hbm_docs = TextLoader("./hbm.txt", encoding="utf-8").load()
    nvme_docs = TextLoader("./nvme.txt",encoding="utf-8").load()
    docs = hbm_docs + nvme_docs

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

# results = store.similarity_search("HBM이란 무엇인가요?", k=2)
# results = store.similarity_search("HBM의 성능은 어떤가요?", k=3)
retriever = store.as_retriever(search_kwargs={"k": 3})

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", 
        "당신은 문서 기반 Q&A 시스템입니다. 아래 문서만을 참고해서 답하세요."
        "문서에 적합한 내용이 없으면, '모른다' 라고 답변하세요.\n\n문서:\n{context}"),
    ("user", "{question}")
])

# 이 기능은 langchain 어딘가에 있을것
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

chain = (
    RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x["question"])))
    | prompt
    | llm
    | StrOutputParser()
)

print(chain.invoke({"question": "HBM의 성능은 어떤가요?"}))
print('-' * 60)
print(chain.invoke({"question": "NVMe와 HBM은의 다른건가요?"}))

"""
HBM은 채널당 I/O 데이터 전송률이 1 GT/s에서 9.6 GT/s에 이르는 다양한 규격을 가지고 있으며, 스택당 대역폭은 HBM에서 128 GB/s, HBM2에서 307 GB/s, HBM2E에서 461 GB/s, HBM3에서 819 GB/s, HBM3E에서 1229 GB/s, HBM4에서 2048 GB/s에 달합니다. 이러한 높은 대역폭과 I/O 데이터 전송률 덕분에 HBM은 고성능 그래픽 카드와 같은 응용 분야에서 매우 강력한 성능을 발휘합니다.
------------------------------------------------------------
NVMe와 HBM은 서로 다른 기술입니다. NVMe는 비디오 메모리의 데이터 전송을 위한 인터페이스와 프로토콜로, 특히 SSD와 같은 스토리지 장치에서 사용됩니다. 반면, HBM은 고대역폭 메모리로, DRAM의 일종으로 고성능 컴퓨팅에 사용됩니다. HBM은 여러 층으로 쌓아 구성되며, 주로 그래픽 카드와 같은 고성능 요구 사항을 가진 장치에 사용됩니다. 따라서 NVMe는 스토리지 관련 기술이고, HBM은 메모리 반도체 기술입니다.
"""