from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 작명가 입니다."),
    ("user", "다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: {product}")
])

filled_prompt = prompt.format_messages(product="자율주행 자동차")
print("완성된 프롬프트:", filled_prompt)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke(filled_prompt)
print(response.content)

"""
완성된 프롬프트: [SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 자율주행 자동차', additional_kwargs={}, response_metadata={})]
회사의 이름을 위한 몇 가지 제안입니다:

1. **드라이브프리** (DriveFree)
2. **모빌리티 넥스트** (Mobility Next) 
3. **스마트로드** (SmartRoad)
4. **오토임팩트** (AutoImpact)
5. **차세대 드라이브** (NextGen Drive)
6. **자율모션** (AutoMotion)
7. **이노드라이브** (InnoDrive)
8. **로드리더** (RoadLeader)
9. **에코드라이브** (EcoDrive)
10. **미래차원** (Future Dimension)

각 이름은 자율주행 자동차의 혁신성과 미래 지향적인 특성을 반영합니다. 어떤 이름이 가장 마음에 드시나요?
"""