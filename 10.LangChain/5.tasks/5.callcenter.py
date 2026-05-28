# 목적 - 질문 유형에 따라 적합한 항목으로 답변한다.
# 질문 유형 -> 배송조회 상담원
#          -> 결제관련 상담원
#          -> 기술지원 상담원
# RunnableBranch
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
s
load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

def make_chain(role):
    return (
        ChatPromptTemplate.from_messages([
            ("system", role),
            ("user", "{question}")
        ])
        | llm
        | StrOutputParser()
    )

delivery_chain = make_chain("당신은 배송조회 전문 상담원입니다.")
payment_chain = make_chain("당신은 결제관련 전문 상담원입니다.")
tech_chain = make_chain("당신은 기술지원 전문 상담원입니다.")

branch = RunnableBranch(
    (
        lambda x: "배송조회" in x["question"],
        delivery_chain
    ),
    (
        lambda x: "결제관련" in x["question"],
        payment_chain
    ),
    tech_chain
)
