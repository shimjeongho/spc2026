# 목적 - 여행 계획을 작성한다.
# 도시 입력 -> 음식 추천
#          -> 관광지 추천
#          -> 호텔 추천
# 사용자 입력의 OO을 보고, 시간표/동선/교통수단 vs 음식/관광지
# RunnableParallel, RunnableBranch

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

# 체인 생성 함수
def make_chain(role):
    return (
        ChatPromptTemplate.from_messages([
            ("system", role),
            ("user", "{question}")
        ])
        | llm
        | StrOutputParser()
    )
    
# 음식/관광지/호텔   
food_chain = (
    RunnableLambda(lambda x: print(">>> 음식 추천 실행") or x)
    | make_chain("당신은 여행 음식 추천 전문가입니다.")
)

tour_chain = (
    RunnableLambda(lambda x: print(">>> 관광지 추천 실행") or x)
    | make_chain("당신은 여행 관광지 추천 전문가입니다.")
)

hotel_chain = (
    RunnableLambda(lambda x: print(">>> 호텔 추천 실행") or x)
    | make_chain("당신은 여행 호텔 추천 전문가입니다.")
)

parallel_chain = RunnableParallel({
    "food": food_chain,
    "tour": tour_chain,
    "hotel": hotel_chain
})

# 시간표/동선/교통수단
schedule_chain = (
    RunnableLambda(lambda x: print(">>> 일정 생성 실행") or x)
    | make_chain("당신은 여행 일정 전문가입니다.")
)

branch = RunnableBranch(
    (
        lambda x:
            "시간표" in x["question"]
            or "동선" in x["question"]
            or "교통" in x["question"],

        schedule_chain
    ),
    parallel_chain
)

# 예시 질문
questions = [
    "부산 여행 추천해줘",
    "서울 여행 동선 짜줘"
]

# 답변
for q in questions:
    print("질문:", q)
    print("답변:", branch.invoke({"question": q}))
    print('-' * 60)

