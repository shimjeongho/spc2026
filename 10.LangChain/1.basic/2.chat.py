from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI     # Q&A 용으로 사용 (Chat Model = gpt-3.5-turbo)


llm2 = ChatOpenAI(model='gpt-4o-mini')
prompt2 = '게임 회사를 창업하려고 하는데, 이름 후보군을 3개 지어주세요'
result = llm2.invoke(prompt2)
print(llm2.invoke(prompt2))
print(result.content)

"""
좋은 아침입니다.


1. 블루웨이브 게임즈
2. 노바스튜디오
3. 엠파이어 게임즈
.
System: 1. 레전드 게임즈 2. 인터랙티브 스튜디오 3. 환상적인 게임
"""

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
prompt3 = [
    SystemMessage(content="당신은 창의력이 높은 작명가 입니다."),
    HumanMessage(content="게임 회사를 창업하려고 하는데, 이름 후보군을 3개 지어주세요")
]
"""
좋은 아침입니다.
.

1. 블루월드 게임즈
2. 드림플레이 게임스튜디오
3. 에버랜드 인터랙티브
.
System: 1. 드림메이커스(Dream Makers)
2. 인터플레이(Interplay)
3. 루나틱 스튜디오(Lunatic Studio)
"""
result = llm2.invoke(prompt3)
print(llm2.invoke(prompt3))
print(result.content)