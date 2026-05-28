from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "{product}을/를 만드는 회사의 이름을 하나 추천해주세요."
)

llm = ChatOpenAI(model='gpt-4o-mini')

chain1 = prompt | llm | StrOutputParser()
result1 = chain1.invoke({"product": "웹게임"})

print(f"타입: {type(result1)}")  # <class 'str>
print(f"결과: {result1}")

prompt2 = ChatPromptTemplate.from_template(
    "{topic}에 관련된 키워드를 5개만 쉼표로 구분해서 나열해주세요."
)

chain2 = prompt2 | llm | CommaSeparatedListOutputParser()
result2 = chain2.invoke({"topic": "인공지능"})

print(f"타입: {type(result2)}") # <class 'list>
print(f"결과: {result2}")

print('-' * 30)
##############################################
# 위 두개의 다른 체인들을 LCEL로 하나로 합쳐보기
##############################################

prompt_name = ChatPromptTemplate.from_template(
    "{product} 을 만드는 회사의 이름을 하나 추천해주세요. 이름만 답하시오."
)
prompt_slogan = ChatPromptTemplate.from_template(
    "{company_name} 회사의 캐치프레이즈를 만들어주세요. 캐치프레이즈만 답하시오."
)

chain3 = (
    prompt_name 
    | llm 
    | StrOutputParser() 
    | (lambda name: {"company_name": name.strip()}) 
    | prompt_slogan
    | llm
    | StrOutputParser()
)

result3 = chain3.invoke({"product": "친환경 에코백"})
print(f"결과: {result3}")

"""
타입: <class 'langchain_core.messages.base.TextAccessor'>
결과: "픽셀마법사"라는 이름을 추천드립니다! 게임의 재미와 창의력을 담고 있는 느낌을 줄 수 있을 것 같습니다.
타입: <class 'list'>
결과: ['기계학習', '자연어 처리', '딥러닝', '데이터 마이닝', '컴퓨터 비전']
------------------------------
결과: "지구를 위한 작은 실천, 에코프렌드와 함께!"
"""