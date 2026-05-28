# pip install langchain langchain-openai

# langchain.prompt, llm 기타 등등

# langchain <--- 에코시스템
#  로우레벨
#  llm-model
# langchain-openai	lanchain-google
# openai	claude	gemini	llama 등등

# client = OpenAI()	<-- openAI sdk

# llm = OpenAI		<-- langchain
# 			davinch-text-002
# InstructModel gpt 3.5-turbo-instruct

# llm.invoke(prompt)	<-- llm을 호출

# print(result)

# llm = ChatOpenAI()

import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI # 구버전
from langchain_openai import OpenAI # 신버전

load_dotenv()
openai_api_key = os.environ.get('OPENAI_API_KEY')

# llm = OpenAI(model="gpt-4o-mini")# 기본 환경변수 키
llm = OpenAI(model="gpt-4o-mini", temperature=1.0) # 0일수록 일반적, 1일수록 창의적 (보통 실무적으로 1.3을 넘어가지 않음)
# llm = OpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
# llm = OpenAI(model="gpt-4o-mini", api_key=openai_api_key)
# print(llm)

prompt = "오늘 저녁은 무엇을 먹을까요?"
result = llm.invoke(prompt)
print(result)

"""
# llm = OpenAI(model="gpt-4o-mini")

저는 한식, 중식, 양식 모두 좋습니다. 여러분의 추천을 기다립니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋습니다. 여러분의 추천을 기다립니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋습니다. 여러분의 추천을 기다리고 있어요!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다리고 있어요!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천이 궁금합니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다립니다!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다리고 있어요!"

"오늘 저녁은 무엇을 먹을까요? 한식, 중식, 양식 모두 좋아요. 여러분의 추천을 기다리고 있습니다!"
"""

"""
# llm = OpenAI(model="gpt-4o-mini", temperature=1.0)
**
   - 오늘 저녁으로 어떤 음식을 먹을지 고민 중이신가요? 김치찌개, 불고기, 또는 파스타 같은 다른 국제적인 요리도 좋은 선택이 될 수 있습니다. 어떤 음식을 좋아하시나요?

2. **오늘은 어떤 기분인가요?**
   - 오늘의 기분이 어��신지 궁금합니다. 기분이 좋으시다면 어떤 일이 있었나요? 혹은 기분이 좋지 않다면 그 이유를 말씀해 주시면 좋을 것 같습니다.

3. **최근에 무엇을 하셨나요?**
   - 최근에 어떤 일이나 활동을 하셨는지 궁금합니다. 취미나 여행, 새로운 경험에 대해 이야기해 주실 수 있나요?

4. **좋아하는 음악이나 영화는 무엇인가요?**
   - 좋아하는 음악 장르나 영화가 있다면 어떤 것인지 공유해 주시겠어요? 최근에 좋았던 음악이나 영화도 함께 이야기해 보고 싶습니다.

5. **가장 기억에 남는 순간은 언제인가요?**
   - 여러분의 인생에서 가장 기억에 남는 순간이나 특별한 경험은 무엇인지 궁금합니다. 이야기해 주시면
"""