# 목적 - 뉴스를 분석한다.
# 뉴스 입력 -> 요약 
#          -> 감정분석 
#          -> 카테고리 분석
# RunnableParallel
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

parser = StrOutputParser()

summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 뉴스 요약 전문가입니다."),
    ("human", """ 다음뉴스를 3줄로 요약 해주세요. 뉴스:{news}""")
])

summary_chain = (
    summary_prompt
    | llm
    | parser
)

sentiment_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 뉴스 감정분석 전문가입니다."),
    ("human", """ 다음 뉴스의 감정을 분석해주세요.

조건:
- 긍정 / 부정 / 중립 중 하나만 출력
- 이유도 간단히 설명

뉴스:
{news} 
""")
])

sentiment_chain = (
    sentiment_prompt
    | llm
    | parser
)

category_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 뉴스 카테고리 분석 전문가입니다."),
    ("human", """
    다음 뉴스의 카테고리를 분류해주세요.

카테고리 예시:
- 정치
- 경제
- 사회
- 스포츠
- 연예
- IT
- 국제

뉴스:
{news}
""")
])

category_chain = (
    category_prompt
    | llm
    | parser
)

parallel_chain = RunnableParallel({
    "summary": summary_chain,
    "sentiment": sentiment_chain,
    "category": category_chain
})

news_text = """
삼성전자가 새로운 AI 반도체를 공개하며 글로벌 시장 공략에 나섰다.
이번 제품은 기존 대비 연산 속도가 크게 향상되었으며,
전력 효율 또한 개선되었다고 밝혔다.
"""

result = parallel_chain.invoke({
    "news": news_text
})

print("===== 뉴스 요약 =====")
print(result["summary"])

print("\n===== 감정 분석 =====")
print(result["sentiment"])

print("\n===== 카테고리 =====")
print(result["category"])

"""
===== 뉴스 요약 =====
삼성전자가 새로운 AI 반도체를 공개하며 글로벌 시장에 진출한다. 이번 제품은 기존 모델 대비 연산 속도가 크게 향상되고 전력 효율도 개선되었다. 이를 통해 시장 경쟁력을 높일 계획이다.

===== 감정 분석 =====
긍정

이유: 뉴스 내용은 삼성전자가 새로운 AI 반도체를 공개하며 성능이 향상되었음을 강조하고 있어, 기업의 기술 발전과 시장 공략에 대한 긍정적인 전망을 제시하고 있습니다.

===== 카테고리 =====
이 뉴스의 카테고리는 **IT**로 분류할 수 있습니다. 삼성전자의 AI 반도체와 관련된 내용이 기술 및 정보기술 분야와 밀접하게 관련되어 있습니다.s
"""