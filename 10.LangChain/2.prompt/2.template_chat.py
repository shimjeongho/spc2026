from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 작명가 입니다."),
    ("user", "다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: {product}")
])

filled_prompt = prompt.format_messages(product="스마트폰")
print("완성된 프롬프트:", filled_prompt)

filled_prompt = prompt.format_messages(product="자율주행 자동차")
print("완성된 프롬프트:", filled_prompt)

print('-' * 50)

test_products = [
    "모바일 게임",
    "로봇 장난감",
    "가방",
    "영어 교육 플랫폼",
    "전기 자전거"
]

for product in test_products:
    final_prompt = prompt.format_messages(product=product)

    print(f"[{product}]")
    print(final_prompt)

"""
완성된 프롬프트: [SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 스마트폰', additional_kwargs={}, response_metadata={})]
완성된 프롬프트: [SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 자율주행 자동차', additional_kwargs={}, response_metadata={})]
--------------------------------------------------
[모바일 게임]
[SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 모바일 게임', additional_kwargs={}, response_metadata={})]
[로봇 장난감]
[SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 로봇 장난감', additional_kwargs={}, response_metadata={})]
[가방]
[SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 가방', additional_kwargs={}, response_metadata={})]
[영어 교육 플랫폼]
[SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 영어 교육 플랫폼', additional_kwargs={}, response_metadata={})]
[전기 자전거]
[SystemMessage(content='당신은 작명가 입니다.', additional_kwargs={}, response_metadata={}), HumanMessage(content='다음 상품을 만드는 회사의 이름을 지어주세요. 상품명: 전기 자전거', additional_kwargs={}, response_metadata={})]
"""