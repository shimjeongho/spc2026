import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAI         # 단발성 질문 (Instruct Model = gpt-3.5-turbo-instruct)
from langchain_openai import ChatOpenAI     # Q&A 용으로 사용 (Chat Model = gpt-3.5-turbo)

llm = OpenAI(model='gpt-3.5-turbo-instruct')
prompt = '다음 문장을 한국말로 번역해줘: Good Morning'
print(llm.invoke(prompt))

"""
, I hope you have a great day today! 
```

이렇게 작성하시면 됩니다. 추가적인 질문이나 요청이 있으면 언제든지 말씀해 주세요!

네, 맞습니다! 여기 번역된 문장입니다:

"좋은 아침입니다. 오늘 하루도 ��지게 보내시길 바랍니다!" 

더 필요한 부분이 있으면 말씀해 주세요!
"""

llm2 = ChatOpenAI(model='gpt-4o-mini')
prompt2 = '게임 회사를 창업하려고 하는데, 이름 후보군을 3개 지어주세요'
print(llm.invoke(prompt2))

"""
.


1. 블루월드 게임즈
2. 픽셀마스터 게임스튜디오
3. 인피니티 게임웍스
.
"""

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
prompt3 = [
    SystemMessage(content="당신은 창의력이 높은 작명가 입니다."),
    HumanMessage(content="게임 회사를 창업하려고 하는데, 이름 후보군을 3개 지어주세요")
]
"""
System: 1. "무한스테이지" - 게임의 끝이 없는 재미를 암시하는 이름
2. "드림 메이커" - 꿈을 현실로 만들어주는 게임의 감동적인 경험을 나타내는 이름
3. "퍼즐 파라다이스" - 다양한 퍼즐과 게임 요소가 결합된 파라다이스 같은 게임 세계를 상상케하는 이름
"""

print(llm.invoke(prompt3))