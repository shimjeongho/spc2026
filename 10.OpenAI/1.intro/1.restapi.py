import requests
import os

openai_api_key = os.getenv('OPENAI_API_KEY')
user_input = "우리집에 새로운"

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    json={
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': '너는 나를 잘 도와주는 경력 20년차의 작명가야.'},
            {'role': 'user', 'content': user_input}
        ],
        'temperature' : 1.0,
        'top_p': 0.5
    },
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}'     # Basic 인증 = Basic Authorization
    }
)

data = response.json()
final_response = data['choices'][0]['message']['content']

# print(response)
"""
<Response [200]>
"""
print(final_response)
"""
안녕하세요! 전문가로서 호텔 쉐프로서 여러 영역에서 도와드릴 수 있습니다. 식사 아이디어나 조리법, 식재료 추천, 음식 서빙 방법, 식사 계획 및 이벤트 구성 등 다양한 요리와 식음료 관련 질문에 대해 도와드릴 수 있습니다. 어떤 분야에서 도와드리면 좋을지 또는 궁금한 내용이 있으신가요? 질문이 있으면 언제든지 물어봐 주세요!
"""