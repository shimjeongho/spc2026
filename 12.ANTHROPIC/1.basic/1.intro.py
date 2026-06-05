# pip install anthropic
import os

#import openai
import anthropic

from dotenv import load_dotenv

load_dotenv()

# client = openai.OpenAI()
client = anthropic.Anthropic()

# message = client.chat.completion
message = client.messages.create(
    #haiku(빠름), sonnet, opus(최신, 고성능)
    model="claude-haiku-4-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "안녕! 한 문장으로 너를 소개해줘."
        }
    ]
)

print(message.content[0].text)
"""
안녕하세요! 저는 OpenAI의 Claude로, 질문에 답하고 다양한 작업을 도와드리는 AI 어시스턴트입니다.
"""