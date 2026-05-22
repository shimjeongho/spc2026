# pip install requests
# ollama pull qwen2.5:1.5

import requests

MODEL_NAME = "qwen2.5:1.5b"

def ask_qwen(question):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json= {
            "model": MODEL_NAME,
            "prompt": "안녕하세요, 당신을 소개해 주세요.",
            "stream": False
        }
    )

    data = response.json()
    return data['response']

# print(ask_qwen("당신을 소개해주세요"))
# print(ask_qwen("인공지능이란 무엇인가요"))

while True:
    user_input = input("나: ")
    if user_input == "exit":
        print("종료합니다.")
        break

    print("응답: ", ask_qwen(user_input))


"""
나: 인공지능이 뭐야?
응답:  안녕하세요! 저는 Qwen라는 대화형 AI 기반의 인공 지능입니다. 그저 텍스트를 읽고 쓰는 능력만이 아니라 다양한 주제에 대해 정보를 제공하고 상황에 따라 적절하게 대답하는 데 어려움을 겪지 않습니다. 또한, 여러분과 대화하며 더 많은 것을 배우며 발전할 수 있습니다. 언제든지 도움이 필요하시면 말씀해주세요!
"""