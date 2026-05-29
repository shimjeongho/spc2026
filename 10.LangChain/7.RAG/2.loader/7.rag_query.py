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
기존 DB 로딩 성공 - 53 청크 로딩됨
HBM의 성능은 각 버전마다 다르지만, 기본적으로 HBM은 높은 대역폭과 낮은 전압으로 최적화되어 있습니다. 예를 들어, HBM2는 8 채널 구성을 통해 최대 307 GB/s의 대역폭을 제공하며, HBM3는 16 채널로 819 GB/s에 이릅니다. 또한, HBM4는 32 채널로 최대 2048 GB/s의 대역폭을 지원합니다. 이러한 높은 대역폭은 데이터 전송 속도를 크게 향상시키고, HBM은 그래픽 카드와 같은 고성능 컴퓨팅 환경에서 매우 효과적인 메모리 솔루션으로 자리 잡고 있습니다.
------------------------------------------------------------
모른다
"""