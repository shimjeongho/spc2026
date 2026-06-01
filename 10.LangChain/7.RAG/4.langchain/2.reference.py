# 표준 LCEL 로 RAG 모델을 구현하기

import os
from dotenv import load_dotenv

# 채팅
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

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
    # return "\n\n".join(d.page_content for d in docs)
    return "\n\n".join(f"[{i}] {d.page_content}" for i, d in enumerate(docs, start=1)) # 검색된 문서들을 번호와 함께 포맷팅 enumerate로 번호 붙이기

# HW. 아래 코드에서 개별 답변 번호화 참고자료 번호 맞추기... 그래서 중복 레퍼런스도 허용하기
# 이때, 프롬프트에도 명확하게 답변의 번호화 출처의 번호를 맞춰서 답변하시오
# 1.유효함: 출처 x
# 2. 유효하지 않음 : 출처 y
# 3. 유효함 : 출처 z
# 답변: 1, 3번이 유효함. 출처는 각각 x, z
def extract_sources(docs):      # 우리의 소스를 unique하게 출력한다.
    seen, sources =set(), []
    for d in docs:
        src = d.metadata.get("source", "?")
        if src not in seen:
            seen.add(src)
            sources.append(src)

    return sources

def retrieve_and_split(inputs):
    docs = retriever.invoke(inputs["question"])
    return {
        "question": inputs["question"],
        "context": format_docs(docs),
        "sources": extract_sources(docs)
    }


def append_sources(inputs):
    src_lines ="\n".join(f"- {s}" for s in inputs["sources"])
    return f"{inputs['answer']}\n\n 참고문서: \n{src_lines}"

chain = (
    RunnableLambda(retrieve_and_split)
    | RunnablePassthrough.assign(answer=(prompt | llm | StrOutputParser()))
    | RunnableLambda(append_sources) 
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
   - HBM은 메모리 기술로, 주로 그래픽 카드와 고성능 컴퓨팅 시스템에서 사용됩니다.
   - HBM은 높은 대역폭과 낮은 전력 소비를 특징으로 하며, 여러 개의 메모리 다이를 수직으로 쌓아 올려서 구성됩니다.
   - 이는 데이터 전송 속도를 높이고, 메모리 용량을 증가시키는 데 도움을 줍니다.

결론적으로, NVMe는 저장 장치와 관련된 프로토콜인 반면, HBM은 메모리 기술로, 두 기술은 서로 다른 용도와 기능을 가지고 있습니다.

 참고문서: 
- nvme.txt
- hbm.txt
"""