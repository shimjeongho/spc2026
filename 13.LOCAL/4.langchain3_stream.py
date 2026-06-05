# pip install langchain-openai langchain-anthopic (이것처럼 ollama도 따로 있음)
# pip install langchain-ollama

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="mistral")

prompt = PromptTemplate.from_template("다음 주제로 작성할만한 블로그 글의 개요를 5가지 만들어줘. 답변은 꼭 한국말로 해줘.\n\n주제: {topic}")

chain = prompt | llm | StrOutputParser()

for chunk in chain.stream({"topic": "로컬 LLM 모델 활용"}):
    print(chunk, end="", flush=True)

"""
 1. 로컬 LLM(Language Model) 모델 사용 이론 및 설명
   - 글 소개: 자연어 처리(NLP)의 중요한 기술 중 하나인 언어 모델(Language Model)에 대해, 로컬 LLM이란 무엇인지, 사용 방법, 장점 및 단점을 설명합니다.

2. 로컬 LLM 모델의 활용예: 채팅봇 개발
   - 글 소개: 로컬 LLM 모델은 자연어 처리 기술을 활용한 채팅봇 개발에 유용합니다. 이 글에서는 로컬 LLM 모델을 사용하여 채팅봇을 구축하는 방법과 예시를 소개합니다.

3. 로컬 LLM 모델의 활용예: 웹 문서 summarization
   - 글 소개: 대량의 정보가 있는 웹 문서를 요약하여 효과적으로 사용할 수 있습니다. 이 글에서는 로컬 LLM 모델을 활용한 웹 문서 summarization의 개념, 방법, 장점 및 단점을 소개합니다.

4. 로컬 LLM 모델 학습 방법
   - 글 소개: 로컬 LLM 모델의 효과적인 활용을 위해서는 모델의 학습이 필요합니다. 이 글에서는 로컬 LLM 모델을 학습하는 방법, 데이터 준비, 학습 환경, 훈련 및 테스트를 포함한 세부 단계를 설명합니다.

5. 로컬 LLM 모델 선택 기준과 추천 도구
   - 글 소개: 로컬 LLM 모델을 선택하는 데에는 몇 가지 기준이 있습니다. 이 글에서는 로컬 LLM 모델 선택의 중요 매개변수와, 대표적인 도구 및 라이브러리를 소개합니다. 추가로 각 도구의 장점과 단점을 비교하여 로컬 LLM 모델 선택에 유용한 정보를 제공합니다.
"""