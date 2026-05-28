# 목적: 긴 문장을 받아서 짧게 요약한다.
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate
)

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

template = "다음의 긴 내용을 3개의 문장으로 요약하시오:\n\n{article}"
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신은 전문 문장 요약가 입니다."),
    HumanMessagePromptTemplate.from_template(template)
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)  # 이런 경우 0.3~0.5 정도를 쓴다.

chain = chat_prompt | llm | RunnableLambda(lambda x: {"summary": x.content.strip()})

input_text = {
    "article": "김광현 네이버 최고데이터·콘텐츠책임자(CDO)는 28일 서울 중구 더플라자 호텔에서 열린"
               "'AI 시대 네이버의 데이터·콘텐츠 전략' 미디어 라운드 테이블에 참석해 "
               "창작자 생태계와 외부 파트너십을 통해 실행형 에이전트의 기반이 되는 양질의 데이터를 잘 쌓고"
               ", 이를 AI와 연결해 차별화된 사용자 경험을 제공하겠다"
               "고 말했다."
}

result = chain.invoke(input_text)
print("요약 결과: ", result["summary"])

"""
요약 결과:  김광현 네이버 최고데이터·콘텐츠책임자(CDO)는 'AI 시대 네이버의 데이터·콘텐츠 전략' 미디어 라운드 테이블에서 발언했다. 그는 창작자 생태계와 외부 파트너십을 통해 양질의 데이터를 구축하고 이를 AI와 연결하여 차별화된 사용자 경험을 제공할 계획을 밝혔다. 이를 통해 네이버는 실행형 에이전트의 기반을 다질 예정이다.
"""