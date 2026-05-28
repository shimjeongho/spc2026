from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 상품명을 지어주는 기획자 입니다."),
    ("user", "{company} 회사에서 {product}을 만드는데, 이 제품명을 만들어주시오.")
])

chain = prompt | llm | parser | RunnableLambda(lambda x: {"response": x})

inputs = {"company": "AI 첨단 기술 회사", "product": "화장품"}

result = chain.invoke(inputs)

print("최종결과: ", result)

"""
최종결과:  {'response': "물론입니다! AI 첨단 기술을 활용한 화장품을 위해 다음과 같은 제품명을 제안드립니다:\n\n1. **Aesthetic AI** - 아름다움과 인공지능의 조화를 강조한 이름.\n2. **SkinSync** - 피부와 AI가 완벽하게 조화를 이루는 제품이라는 의미.\n3. **GlowTech** - 빛나는 피부를 위한 첨단 기술을 나타내는 이름.\n4. **DermaGenius** - 피부를 위한 천재적인 솔루션을 강조.\n5. **InnoGlow** - 혁신적인 아름다움을 전달하는 화장품.\n6. **AIvitalize** - AI로 활력을 주는다는 의미를 담은 이름.\n7. **CuraAI** - 'Cura'는 라틴어로 케어를 의미하며, AI 기술을 결합한 이름.\n8. **Elysian Essence** - 천상의 아름다움을 수호한다는 뜻을 담은 명칭.\n9. **SmartRadiance** - 스마트한 기술로 빛나는 피부를 이끌어내는 제품.\n10. **TechniQ Skin** - 기술력(Q)으로 혁신적인 피부 관리를 제공하는 의미.\n\n이 중에서 마음에 드는 이름을 선택하시거나, 제가 더 많은 아이디어를 제안해 드릴 수도 있습니다!"}
"""