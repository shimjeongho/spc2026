# 텍스트를 기반으로 이미지를 생성... (GAN)

# 구버전 모델이 dall-e => dall-e-2 => ??
# gpt-image-1.5 또는 gpt-image-2
#

import os
import base64

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# prompt="""
# 노을 지는 해변, 잔잔한 파도, 수체화 스타일,
# 돌고래 3마리가 파도를 헤엄치다가 그중 한마리가 점프해서 날개를 달고 한마리를 잡아먹고 있음. 파도는 3층
# """

prompt = """
아이콘팩을 4x4로 해서 16개를 만들고 64x64 크기로 해서, 해변, 조개, 소라 등의 사물을 통해서 웹서비스 개발에 위한 아이콘 팩을 만들어줘.
"""

result = client.images.generate(
    model = "gpt-image-1.5",
    prompt = prompt,
    size='1024x1024',   # 1024x1024(정사각형), 1024x1536(세로), 1536x1024(가로)
    quality='high'    # low / medium / high / auto
)

# image-2
# 4k까지 지원함 (4096) 16:9 비율도 생성 가능
# 지원 언어가 대폭 증가
# 빠진 단점 하나는, 투명배경 못만듦,  투명배경을 1.5의 기능임

b64 = result.data[0].b64_json
# with open('output.png', 'wb') as f:      # 노을 지는 해변, 잔잔한 파도, 수체화 스타일
# with open('shpark1.png', 'wb') as f:       # 노을 지는 해변, 잔잔한 파도, 수체화 스타일, 돌고래 3마리가 파도를 헤엄치다가 그중 한마리가 점프해서 날개를 달고 한마리를 잡아먹고 있음. 파도는 3층
with open('icon.png', 'wb') as f:       # 아이콘팩을 4x4로 해서 16개를 만들고 64x64 크기로 해서, 해변, 조개, 소라 등의 사물을 통해서 웹서비스 개발에 위한 아이콘 팩을 만들어줘.
    f.write(base64.b64decode(b64))

print('저장 완료')
