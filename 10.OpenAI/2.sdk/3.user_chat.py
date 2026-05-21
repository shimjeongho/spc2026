# pip uninstall openai; pip install openai       # 현재 최신은 4.x
import openai

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai_api_key)

def ask_chatbot(user_input):

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': '당신의 나의 질문에 답변을 잘 하는 챗봇입니다.'},
            {'role': 'user', 'content': user_input}
        ]
    )

    final_response = response.choices[0].message.content
    return final_response

while True:
    user_input = input("\n질문: ").strip()
    chatbot_response = ask_chatbot(user_input)
    print("챗봇응답: ", chatbot_response)

"""
질문: 나는 누구니
챗봇응답:  저는 챗봇인 아바타입니다. 궁금한 것이 있거나 이야기를 나누고 싶은 것이 있으면 언제든지 말씀해주세요!

질문: 나는 고양이야
챗봇응답:  고양이라니, 멋진 동물이죠! 고양이들은 귀여운 외모와 깜놀란 행동으로 사람들을 매료시킵니다. 고양이들이 어떤 모습인지 궁금하신가요?

질문: 그래서 내가 누구라고?
챗봇응답:  당신은 현재 이 챗봇과 대화 중인 사용자입니다. 당신의 신원과 관련된 다른 정보는 저에게는 없습니다. 어떤 질문이든지 자유롭게 해주시면 저는 최선을 다해 도와드리겠습니다.
"""