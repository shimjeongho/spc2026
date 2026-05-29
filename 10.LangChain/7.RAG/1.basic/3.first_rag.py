from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

docs = [
    Document(page_content="NVMe는 SSD 의 인터페이스 규격으로 PCIe를 사용한다."),
    Document(page_content="SATA SSD는 NVMe 보다 속도가 느리다."),
    Document(page_content="HDD는 회전 디스크 기반이라 IO가 느린 편이다."),
    Document(page_content="파이썬은 인기 있는 프로그래밍 언어다."),
    Document(page_content="자바스크립트는 브라우저에서 동작하는 언어이다."),
    Document(page_content="Rust는 메모리 안정성과 성능을 동시에 추구한다.")
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
store = InMemoryVectorStore.from_documents(docs, embedding=embeddings)

query = "NVMe 와 SATA의 차이는 무엇인가요?"
results = store.similarity_search(query, k=3)  # 위 질문과 가장 가까운 문서 3개를 골라주시오.

print(f"질문: {query}\n")
print(f"가장 가까운 {len(results)} 개의 문서")
for i, doc in enumerate(results, 1):
    print(f" {i}. {doc.page_content}")

# ============================================================================================================= 

# 검색 결과 합치기
context = "\n".join(doc.page_content for doc in results)

prompt = ChatPromptTemplate.from_template("""
아래 문서를 참고하여 질문에 답하시오.
                                                 
문서:
{context}
                                                 
질문:
{question}
                                                 
""")

chain = prompt | llm
answer = chain.invoke({
    "context": context,
    "question": query
})

print(answer.content)

"""
질문: NVMe 와 SATA의 차이는 무엇인가요?

가장 가까운 3 개의 문서
 1. SATA SSD는 NVMe 보다 속도가 느리다.
 2. NVMe는 SSD 의 인터페이스 규격으로 PCIe를 사용한다.
 3. HDD는 회전 디스크 기반이라 IO가 느린 편이다.
NVMe와 SATA의 차이는 주로 데이터 전송 방식과 속도에서 나타납니다.

1. **인터페이스 규격**: NVMe는 PCIe(Peripheral Component Interconnect Express)를 사용하여 더 빠른 데이터 전송을 지원합니다. 반면 SATA(SERIAL ATA)는 구식 인터페이스로, SSD에 비해 속도가 상대적으로 느립니다.

2. **속도**: NVMe SSD는 SATA SSD보다 속도가 빠릅니다. SATA SSD는 NVMe SSD보다 느린 IO 성능을 가진 반면, NVMe는 더 높은 대역폭과 짧은 지연 시간을 제공합니다.

3. **기술적 특성**: NVMe는 SSD의 특성을 최대한 활용하도록 설계된 프로토콜로, 더 많은 명령을 동시에 처리할 수 있어 전반적인 성능이 향상됩니다. SATA는 HDD와 호환성을 유지하기 위한 설계로, 속도 측면에서 한계를 가지고 있습니다. 

결론적으로, NVMe는 더 빠르고 효율적인 데이터 전송을 제공하는 최신 인터페이스인 반면, SATA는 구형 인터페이스로 상대적으로 느린 속도를 가지고 있습니다.
"""