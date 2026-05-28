from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

template = "당신은 작명가 입니다. {product}를 만드는 회사의 이름을 지어주세요."

prompt = PromptTemplate(input_variables=['product'], template=template)

filled_prompt = prompt.format(product="스마트폰")

print("완성된 프롬프트: ", filled_prompt)