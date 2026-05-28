import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)

from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신의 브랜딩 컨텐츠 기획자 입니다."),
    HumanMessagePromptTemplate.from_template("회사를 홍보하기 위한 {company} 회사의 {product} 상품을 기반으로 캐치프레이즈를 만들어 주세요.")
])

llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

# 아래 체이닝 문법을 LCEL (LangChain Expression Language) 라고 부름
chain = prompt | llm | parser

# chain = prompt | llm | StrOutputParser()   # parser = StrOutputParser() 정의 안하고 그대로도 사용 가능


# inputs = {"company":"삼성전자", "product":"메모리"}
inputs = {"company":"하이닉스", "product":"HBM"}

result = chain.invoke(inputs) # <-- 여기가 핵심. 모든값 체인을 호출(invoke) 하면서 실행함.

final_result = {"response": result}
print(final_result)
