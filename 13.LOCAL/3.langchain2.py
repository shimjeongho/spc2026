# pip install langchain-openai langchain-anthopic (이것처럼 ollama도 따로 있음)
# pip install langchain-ollama

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="mistral")

prompt = PromptTemplate.from_template("다음 주제로 작성할만한 블로그 글의 개요를 5가지 만들어줘. 답변은 꼭 한국말로 해줘.\n\n주제: {topic}")

chain = prompt | llm | StrOutputParser()

print(chain.invoke({"topic": "로컬 LLM 모델 활용"}))

"""
 1. **"로컬 LLM(Language Model) 모델의 기본 개념 및 유용성"**
    - 이 포스트에서는 로컬 Language Model(LLM)을 소개하고, 그 필요성과 사용 방법에 대해 설명합니다. LLM은 자연어 처리 분야의 중요한 기술이며, 시계열 데이터 처리에서 활용되는 모델입니다.

2. **"로컬 LLM 모델을 활용한 여러 분야의 예"**
    - 이 포스트에서는 로컬 Language Model(LLM)을 적용한 다양한 분야를 소개합니다. 예시로, 문자 수동 번역, 글꼴 생성, 게시판 스파
"""