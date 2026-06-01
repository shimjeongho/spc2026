# 표준 LCEL 로 RAG 모델을 구현하기

import os
from dotenv import load_dotenv

# 채팅
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 임베딩
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

# 1. 백터 스토어(DB) 정의하기
DB_DIR = "./chroma_db"
COLLECTION_NAME = "my_rag"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

store = Chroma(collection_name=COLLECTION_NAME, embedding_function=embeddings, persist_directory=DB_DIR)

if store._collection.count() == 0:
    docs = TextLoader("./nvme.txt", encoding="utf-8").load() \
         + TextLoader("./hbm.txt", encoding="utf-8").load()
    
    chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(docs)
    for c in chunks:
        c.metadata["source"] = os.path.basename(c.metadata.get("source", "?")) 

    store.add_documents(chunks)

retriever = store.as_retriever(search_kwargs={"k": 3})

# 2. LLM + 프롬프트 설계하기
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ("system", 
        "당신은 문서 기반 Q&A 시스템입니다. 아래 문서만을 참고해서 답변하시오."),
    ("user", "{question}")
])

# 3. 표준 질의응답을 위한 파이프라임 설계 (체이닝)
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)
chain = (
    RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x["question"]))) |  # 검색
    prompt |
    llm |
    StrOutputParser()
)

# 4. 최종 질문
print(chain.invoke({"question": "NVMe와 HBM의 차이는??"}))

"""
NVMe(Non-Volatile Memory Express)와 HBM(High Bandwidth Memory)은 각각 다른 목적과 기능을 가진 기술입니다.

1. **NVMe**:
   - NVMe는 저장 장치와 CPU 간의 데이터 전송을 위한 인터페이스 프로토콜입니다.
   - 주로 SSD(솔리드 스테이트 드라이브)와 같은 비휘발성 메모리 장치에서 사용됩니다.
   - NVMe는 높은 속도와 낮은 지연 시간을 제공하여 데이터 전송 효율성을 극대화합니다.

2. **HBM**:
   - HBM은 고대역폭 메모리 기술로, 주로 그래픽 카드와 고성능 컴퓨팅 시스템에서 사용됩니다.
   - HBM은 메모리 칩을 수직으로 쌓아 높은 대역폭을 제공하며, 전력 효율성도 높습니다.
   - HBM은 데이터 처리 속도를 높이기 위해 설계되었으며, 대량의 데이터를 빠르게 처리할 수 있습니다.

결론적으로, NVMe는 저장 장치와의 데이터 전송을 위한 프로토콜인 반면, HBM은 메모리 기술로서 데이터 처리 속도를 높이는 데 중점을 둡니다.
"""