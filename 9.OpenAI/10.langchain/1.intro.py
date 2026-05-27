# pip install langchain langchain-openai

import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI # 구버전
from langchain_openai import OpenAI # 신버전

load_dotenv()
# open_api_key = os.environ.get('OPENAI_API_KEY')

llm = OpenAI(model="gpt-4o-mini")
# print(llm)

prompt = "오늘 저녁은 무엇을 먹을까요?"
result = llm.invoke(prompt)
print(result)

"""
저는 한식, 중식, 양식 모두 좋습니다. 여러분의 추천을 기다립니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋습니다. 여러분의 추천을 기다립니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋습니다. 여러분의 추천을 기다리고 있어요!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다리고 있어요!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천이 궁금합니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다립니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다리고 있어요!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다리고 있습니다!"
"""