from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI     # Q&A 용으로 사용 (Chat Model = gpt-3.5-turbo)
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


llm = ChatOpenAI(model='gpt-4o-mini')

prompt = [
    SystemMessage(content="당신은 창의력이 높은 작명가 입니다."),
    HumanMessage(content="게임 회사를 창업하려고 하는데, 이름 후보군을 3개 지어주세요"),
    AIMessage(content="비빔밥은 어떤신가요?"),
    HumanMessage(content="아~ 좋아. 그걸 만들기 위한 재료는 무엇인가?")
]

result = llm.invoke(prompt)
print(result.content)

"""
비빔밥을 만들기 위한 재료는 다음과 같습니다:

1. **밥**: 기본적인 탄수화물로, 보통 흰 쌀밥을 사용합니다.
2. **채소**: 다양한 나물이나 채소를 준비합니다. 대표적으로 시금치, 고사리, 표고버섯, 당근, 오이, 콩나물 등이 있습니다.
3. **고기**: 주로 불고기나 다진 쇠고기를 볶아서 사용합니다. 채식주의자를 위해 고기를 생략할 수도 있습니다.
4. **계란**: 보통 반숙 계란이나 프라이를 얹어 줍니다.
5. **고추장**: 맛을 내는 메인 양념으로, 매운맛을 추가해 줍니다.
6. **참기름**: 고소한 맛을 더해주는 오일입니다.
7. **깨**: 토핑으로 사용하는 깨소금입니다.

이 재료들을 모두 섞어 맛있게 비벼 먹으면 훌륭한 비빔밥이 완성됩니다!
"""