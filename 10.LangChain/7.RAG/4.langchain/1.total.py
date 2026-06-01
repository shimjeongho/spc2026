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
        "당신은 문서 기반 Q&A 시스템입니다. 아래 문서만을 참고해서 답변하시오."
        "문서에 필요한 내용이 없으면 '모른다' 라고 답하시오.\n\n문서:\n{context}"),
    ("user", "{question}")
])


# 3. 표준 질의응답을 위한 파이프라임 설계 (체이닝)
def format_docs(docs):
    return "\n---\n".join(d.page_content for d in docs)

def debug_prompt(prompt):
    print("\n==== LLM에 들어갈 입력값 (즉 PROMPT) ====")
    for msg in prompt.messages:
        print(f"[{msg.type.upper()}]")
        print(msg.content)
    print("\n==== 출력 끝 ====\n")
    return prompt

chain = (
    RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x["question"]))) |  # 검색
    prompt |
    RunnableLambda(debug_prompt) |
    llm |
    StrOutputParser()
)

# 4. 최종 질문
# print(chain.invoke({"question": "NVMe와 HBM의 차이는??"}))
# print(chain.invoke({"question": "NVMe와 SSD의 차이는??"}))
print(chain.invoke({"question": "HBM와 NVMe의 제조사는??"}))

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

"""
[HUMAN]
NVMe와 SSD의 차이는??

==== 출력 끝 ====

NVMe는 비휘발성 저장장치들을 위한 통신 프로토콜이며, SSD는 비휘발성 저장장치의 한 종류입니다. 즉, NVMe는 SSD가 데이터를 전송하는 방식을 정의하는 프로토콜이고, SSD는 데이터를 저장하는 장치입니다. NVMe는 주로 PCI Express 인터페이스를 통해 SSD와 연결되어 성능을 최적화합니다.

==== LLM에 들어갈 입력값 (즉 PROMPT) ====
[SYSTEM]
당신은 문서 기반 Q&A 시스템입니다. 아래 문서만을 참고해서 답변하시오.문서에 필요한 내용이 없으면 '모른다' 라고 답하시오.

문서:
NVMe 1.2부터는 자체 DRAM이 없을 때 시스템의 D램을 끌어와서 페이지 매핑 테이블 저장용 캐시 메모리로 사용하는 HMB가 개발되어 디램리스 NVMe SSD의 성능 저하가 디램리스 SATA에 비해 적어졌다.
---
HMC보다 쉬운 구현 난이도
HBM은 프로세서의 바로 위로 적층하는 것은 불가능하여 완전한 원칩은 구현할 수 없다. 이를 구현하는 것을 목표로 하는 마이크론의 HMC(Hybrid Memory Cube)와 비교했을 때 다소 완전하지 않은 모습으로 인해 3D가 아닌 2.5D라고 불리기도 한다. 하지만 HMC는 기술적으로 구현이 매우 어려워 존재감이 미미한 상태인 반면, HBM은 현재 삼성전자와 SK하이닉스가 대량 생산하고 있으며, AMD와 NVIDIA의 그래픽 카드에 채택되는 등 활약을 하고 있다. 또한 프로세서에도 TSV를 통과시켜야 하는 HMC에 비해서 단순히 인터포저 위에 올리기만 하면 되어 구현 난이도가 비교적 낮다는 것과, HBM이 그래픽 카드 업체에게 보다 사용하기 편한 것이 HBM의 성공에 보탬이 되었다.
DDR RAM보다 강력한 보안
---
GDDR과 비교해 보면 근본적인 구조의 차이로 인해 대역폭 면에서 HBM이 월등하게 우수하다. 삼성은 스택당 최대 8-Hi, 최대 3.2 GT/s, 410 GB/s, 총 16 GB를 지원하는 플래시볼트 HBM2E를 2020년 2월에 양산할 수 있게 되었다. SK하이닉스도 스택당 최대 8-Hi, 최대 3.6 GT/s, 460 GB/s, 총 16 GB를 지원하는 HBM2E를 개발하여 2020년 7월 대량 생산에 돌입했다고 한다. 그리고 2020년 11월 16일, NVIDIA가 전송속도 3.2 Gbps, 대역폭 2 TB/s의 HBM2E로 업그레이드된 A100 80 GB 연산 카드를 발표했다.
3.3. 2023년 이전[편집]
"""

"""
[HUMAN]
HBM와 NVMe의 제조사는??

==== 출력 끝 ====

HBM의 제조사는 SK하이닉스와 삼성이며, NVMe에 대한 제조사는 문서에 언급되어 있지 않습니다.
"""