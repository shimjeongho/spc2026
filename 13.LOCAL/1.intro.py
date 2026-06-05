# pip install ollama

import ollama

ollama.pull("mistral")
response = ollama.chat(model="mistral", messages=[
    {"role": "user", "content": "인공지능에 대해서 설명해줘"}
])

print(response["message"]["content"])

"""
인공지능(Artificial Intelligence, AI)은 인간의 고급 사고능력을 심층적으로 모방하거나 시뮬레이션하는 기계적, 프로그램이나 알고리즘을 의미합니다. AI는 기계가 인간과 같은 사고능력을 갖추고, 문제해결, 학습, 대화, 시각및 음성인식, 로 
"""