from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 상품명을 지어주는 기획자 입니다."),
    ("user", "{company} 회사에서 {product}을 만드는데, 이 제품명을 만들어주시오.")
])

chain = prompt | llm | parser       # <-- 이걸 LCEL (LangChain Expression Langage)

inputs = {"company": "AI 첨단 기술 회사", "product": "화장품"}

result = chain.invoke(inputs)

print("최종결과: ", result)

"""
최종결과:  물론입니다! AI 첨단 기술을 활용한 화장품에 어울리는 몇 가지 제품명을 제안드립니다:

1. **AI드림 스킨 (AIDream Skin)** - 혁신적인 기술이 꿈꾸는 완벽한 피부.
2. **인텔리젼스 뷰티 (Intelligence Beauty)** - 지능형 포뮬러로 아름다움을 밝혀내다.
3. **퓨처 글로우 (Future Glow)** - 미래의 기술로 얻는 현재의 빛나는 피부.
4. **테크노듀 파운데이션 (TechnoDew Foundation)** - 첨단 기술이 빚어내는 수분과 광채.
5. **에버리프 레볼루션 (Everleaf Revolution)** - 지속 가능한 혁신을 통한 건강한 아름다움.
6. **코스메틱스 2.0 (Cosmetics 2.0)** - 진화한 화장품의 새로운 패러다임.
7. **스마트스킨 엘릭서 (SmartSkin Elixir)** - 지능형 성분으로 피부를 케어하다.
8. **넥스트 제너이션 뷰티 (Next Generation Beauty)** - 다음 세대의 뷰티 솔루션.

이 중에서 마음에 드시는 이름이 있길 바랍니다! 추가적인 요구사항이나 특정 단어를 포함하고 싶으시다면 언제든지 말씀해 주세요.
"""