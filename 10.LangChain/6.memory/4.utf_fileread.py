import json
import sys

with open("history.json", "r", encoding="utf-8")as f:
    messages = json.load(f)

ROLE = {"human": "사용자", "ai": "챗봇", "system": "시스템"}

print(f"=== {len(messages)} 메시지 ===")
for i, m in enumerate(messages, 1):
    role = ROLE.get(m.get("type"))
    content = m.get("data").get("content")
    print(f"{i:02d}. [{role:<6}] {content}")

"""
=== 8 메시지 ===
01. [사용자   ] 안녕하세요
02. [챗봇    ] 안녕하세요! 어떻게 도와드릴까요?
03. [사용자   ] 제 이름은 곽길동 입니다.
04. [챗봇    ] 반갑습니다, 곽길동님! 무엇을 도와드릴까요?
05. [사용자   ] 저는 겨울에 바닷가에 가서 서핑하는것을 좋아합니다.
06. [챗봇    ] 겨울에 바닷가에서 서핑하다니 정말 멋진 취미네요! 겨울 바다에서의 서핑은 다른 계절과 또 다른 매력이 있을 것 같아요. 서핑을 하면서 어떤 경험이 가장 기억에 남았나요?
07. [사용자   ] 제 이름과 취미가 뭐라고 했죠??
08. [챗봇    ] 곽길동님, 겨울에 바닷가에 가서 서핑하는 것을 좋아한다고 말씀하셨습니다! 맞나요? 혹시 더 이야기하고 싶은 내용이 있으신가요?
"""