from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 입력 -> A -> B -> C -> D -> 결과
from langchain_core.runnables import RunnablePassthrough


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
retriever = store.as_retriever(search_kwargs={"k": 3})

prompt = ChatPromptTemplate.from_template("""
아래 문서를 참고하여 질문에 답하시오.\n\n        
문서:\n{context}\n\n                             
질문:{question}                                            
""")

def format_docs(docs):
    """ 검색된 Document 리스트를 -> 하나의 문자열로 변환한다 """
    return "\n\n".join(d.page_content for d in docs)

# [Document(...), Document(...), Document(...),] =>
# HDD는 회전 디스크 기반이라 IO가 느린 편이다.

# 파이썬은 인기 있는 프로그래밍 언어다.
# ...


chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough() # 질문을 다음 파이프라인으로도 그대로 전달함
    }
    | prompt
    | llm
    | StrOutputParser()
)

# question = "NVMe 와 SATA의 차이는 무엇인가요?"
# question = "파이썬은 인기 있는 프로그래밍 언어다."
question = "파인애플은 어떤 과일인가요?."
print(f"사용자질문: {question}")
print(f"챗봇의응답: {chain.invoke(question)}")

"""
#### question = "NVMe 와 SATA의 차이는 무엇인가요?"

사용자질문: NVMe 와 SATA의 차이는 무엇인가요?
챗봇의응답: NVMe와 SATA의 차이는 주로 인터페이스와 속도에 있습니다. NVMe는 PCIe(Peripheral Component Interconnect Express) 인터페이스를 사용하여 데이터 전송 속도가 빠르며, 이는 SSD의 성능을 극대화합니다. 반면에 SATA(Serial Advanced Technology Attachment)는 오래된 기술로, 상대적으로 속도가 느리고 SSD보다 HDD와 더 밀접하게 관련된 인터페이스입니다. 따라서 NVMe SSD는 SATA SSD에 비해 훨씬 더 빠른 데이터 전송 속도를 제공하는 것이 특징입니다.
"""

"""
#### question = "파이썬은 인기 있는 프로그래밍 언어다."

사용자질문: 파이썬은 인기 있는 프로그래밍 언어다.
챗봇의응답: 네, 맞습니다. 파이썬은 인기 있는 프로그래밍 언어입니다.
"""

"""
#### question = "파인애플은 어떤 과일인가요?."

사용자질문: 파인애플은 어떤 과일인가요?.
챗봇의응답: 문서에서는 파인애플에 대한 정보가 없기 때문에 해당 질문에 대한 답변을 제공할 수 없습니다. 파인애플은 열대 과일로, 달콤하고 즙이 많은 특징이 있습니다. 추가적인 정보나 질문이 필요하다면 말씀해 주세요!
"""