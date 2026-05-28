import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)

from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신의 브랜딩 컨텐츠 기획자 입니다."),
    HumanMessagePromptTemplate.from_template("회사를 홍보하기 위한 {company} 회사의 {product} 상품을 기반으로 캐치프레이즈를 만들어 주세요.")
])

llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

# inputs = {"company":"삼성전자", "product":"메모리"}
inputs = {"company":"하이닉스", "product":"HBM"}
messages = prompt.format_messages(**inputs) # company"삼성전자", product="메모리"

response = llm.invoke(messages)
output = parser.invoke(response)

final_result = {"response": output}
print(final_result)

"""
# inputs = {"company":"삼성전자", "product":"메모리"}
{'response': '물론입니다! 삼성전자의 메모리 상품을 홍보하기 위한 몇 가지 캐치프레이즈를 제안드립니다.\n\n1. "미래를 담다, 삼성 메모리!"\n2. "속도와 성능의 혁신, 삼성 메모리와 함께하세요!"\n3. "당신의 꿈을 실현하는 메모리, 삼성의 선택!"\n4. "믿을 수 있는 안정성, 삼성 메모리가 보장합니다!"\n5. "모든 순간을 기억하는 힘, 삼성 메모리!"\n\n이 중에서 마음에 드시는 것이 있거나, 다른 스타일의 제안이 필요하시면 말씀해 주세요!'}
"""

"""
# inputs = {"company":"하이닉스", "product":"HBM"}
{'response': '"HBM, 당신의 혁신을 가속화하는 초고속 메모리!" \n\n혹은 \n\n"하이닉스 HBM, 미래를 열어가는 강력한 데이터 파트너!" \n\n원하는 분위기나 특정 메시지가 있다면 말씀해 주시면 더 맞춤화된 슬로건을 제공해 드릴 수 있습니다!'}
"""