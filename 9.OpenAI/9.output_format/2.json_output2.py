import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'system', 'content': '질문에 대해 JSON으로만 답변하시오.'},
        {'role':'user', 'content':'서울의 인구와 면적을 알려주시오.'},
    ],
    response_format={'type': 'json_object'} # 출력 결과가 OOO 타입이 되도록 API단계에서 보장한다.
)

answer = response.choices[0].message.content
print(answer)

"""
# 불필요한 것들 삭제
{
  "서울": {
    "인구": "약 9,730,000명",
    "면적": "605.21 km²"
  }
}"""
