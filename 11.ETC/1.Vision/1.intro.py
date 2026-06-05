# 방법
# 1. 사진을 직접 올린다 (base64 인코딩)
# 2. 이미지 URL을 주고 읽어가라고 한다.

import os
# 질의 응답 용이 아닌 단발성 용
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Chris_Walker_-_BSB_Snetterton_2009.jpg/250px-Chris_Walker_-_BSB_Snetterton_2009.jpg'

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': '이 이미지를 한국어로 설명해줘'},
                {'type': 'image_url', 'image_url': {'url': image_url}} # 이 줄이 핵심 
            ]
    
        }
    ]
)

print(response)

"""
'이 이미지는 경주용 오토바이를 타고 있는 장면입니다. 오토바이는 현대적인 디자인을 가지고 있으며, 주로 흰색과 파란색으로 도색되어 있습니다. 라이더는 헬멧을 착용하고 있으며, 차량의 사이드에서 번호 "9"가 강조되어 보입니다. 배경에는 잔디와 트랙이 보이며, 속도를 내고 있는 것으로 보입니다
"""