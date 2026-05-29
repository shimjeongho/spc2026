# 목적 - 뉴스를 분석한다.
# 뉴스 입력 -> 요약 
#          -> 감정분석 
#          -> 카테고리 분석
# RunnableParallel
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# load_dotenv()

# llm = ChatOpenAI(model='gpt-4o-mini')

# parser = StrOutputParser()

# summary_prompt = ChatPromptTemplate.from_messages([
#     ("system", "당신은 뉴스 요약 전문가입니다."),
#     ("human", """ 다음뉴스를 3줄로 요약 해주세요. 뉴스:{news}""")
# ])

# summary_chain = (
#     summary_prompt
#     | llm
#     | parser
# )

# sentiment_prompt = ChatPromptTemplate.from_messages([
#     ("system", "당신은 뉴스 감정분석 전문가입니다."),
#     ("human", """ 다음 뉴스의 감정을 분석해주세요.

# 조건:
# - 긍정 / 부정 / 중립 중 하나만 출력
# - 이유도 간단히 설명

# 뉴스:
# {news} 
# """)
# ])

# sentiment_chain = (
#     sentiment_prompt
#     | llm
#     | parser
# )

# category_prompt = ChatPromptTemplate.from_messages([
#     ("system", "당신은 뉴스 카테고리 분석 전문가입니다."),
#     ("human", """
#     다음 뉴스의 카테고리를 분류해주세요.

# 카테고리 예시:
# - 정치
# - 경제
# - 사회
# - 스포츠
# - 연예
# - IT
# - 국제

# 뉴스:
# {news}
# """)
# ])

# category_chain = (
#     category_prompt
#     | llm
#     | parser
# )

# parallel_chain = RunnableParallel({
#     "summary": summary_chain,
#     "sentiment": sentiment_chain,
#     "category": category_chain
# })

# news_text = """
# 삼성전자가 새로운 AI 반도체를 공개하며 글로벌 시장 공략에 나섰다.
# 이번 제품은 기존 대비 연산 속도가 크게 향상되었으며,
# 전력 효율 또한 개선되었다고 밝혔다.
# """

# result = parallel_chain.invoke({
#     "news": news_text
# })

# print("===== 뉴스 요약 =====")
# print(result["summary"])

# print("\n===== 감정 분석 =====")
# print(result["sentiment"])

# print("\n===== 카테고리 =====")
# print(result["category"])

# """
# ===== 뉴스 요약 =====
# 삼성전자가 새로운 AI 반도체를 공개하며 글로벌 시장에 진출한다. 이번 제품은 기존 모델 대비 연산 속도가 크게 향상되고 전력 효율도 개선되었다. 이를 통해 시장 경쟁력을 높일 계획이다.

# ===== 감정 분석 =====
# 긍정

# 이유: 뉴스 내용은 삼성전자가 새로운 AI 반도체를 공개하며 성능이 향상되었음을 강조하고 있어, 기업의 기술 발전과 시장 공략에 대한 긍정적인 전망을 제시하고 있습니다.

# ===== 카테고리 =====
# 이 뉴스의 카테고리는 **IT**로 분류할 수 있습니다. 삼성전자의 AI 반도체와 관련된 내용이 기술 및 정보기술 분야와 밀접하게 관련되어 있습니다.s
# """


# =================================================================================================================================================================
# 위쪽 내 코드 밑에쪽 풀이 코드
# =================================================================================================================================================================
load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

prompt1 = ChatPromptTemplate.from_template("다음 뉴스를 2~3문장으로 요약해줘.\n\n{news}")

#  chain이란 prompt | llm | parser
summary_chain = prompt1 | llm | StrOutputParser()

sentiment_chain = (
    ChatPromptTemplate.from_template("다음 뉴스를 전반적 감성을 한 단어로 분석해줘 (긍정 / 부정 / 중립).\n\n{news}")
    | llm
    | StrOutputParser()
)

category_chain = (
    ChatPromptTemplate.from_template("다음 뉴스를 카테고리를 한 단어로 분석해줘 (정치/경제/사회/스포츠/기타).\n\n{news}")
    | llm
    | StrOutputParser()
)

final_chain = RunnableParallel ({
    "summary": summary_chain,
    "sentiment": sentiment_chain,
    "category" : category_chain
})

news = "국내 증시의 ‘큰손’인 국민연금이 올해 국내주식 목표 비중을 기존 14.9%에서 20.8%로 5.9%포인트 높이기로 했다. 이 목표치보다 폭넓은 운용이 가능하도록 전략적 배분 허용범위(±5%포인트)도 한시적으로 확대하기로 했다. 국내 증시 활황으로 기존 한도를 유지하면 최대 170조원 규모의 주식을 팔아야 하는 부담 등을 고려해 목표 비중을 상향 조정한 것이다."

result = final_chain.invoke({"news": news})

print(f"원문: {news}" )
print(f"요약: {result["summary"]}" )
print(f"감정: {result["sentiment"]}" )
print(f"카테고리: {result["category"]}" )

"""
원문: 국내 증시의 ‘큰손’인 국민연금이 올해 국내주식 목표 비중을 기존 14.9%에서 20.8%로 5.9%포인트 높이기로 했다. 이 목표치보다 폭넓은 운용이 가능하도록 전략적 배분 허용범위(±5%포인트)도 한시적으로 확대하기로 했다. 국내 증시 활황으로 기존 한도를 유지하면 최대 170조원 규모의 주식을 팔아야 하는 부담 등을 고려해 목표 비중을 상향 조정한 것이다.
요약: 국민연금이 올해 국내주식 목표 비중을 14.9%에서 20.8%로 5.9%포인트 높이기로 결정했다. 이를 통해 국내 증시의 활황에 대응하고, 기존 한도를 유지할 경우 발생할 수 있는 170조원의 주식 매각 부담을 줄이려는 전략이다. 또한, 전략적 배분 허용범위도 한시적으로 확대된다.
감정: 이 뉴스는 긍정적인 감성을 가지고 있습니다. (긍정)
카테고리: 경제
"""