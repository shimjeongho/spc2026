from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

@tool
def get_word_length(word: str) -> int:
    """ 단어를 글자 수를 세어서 숫자로 변환한다 """
    return len(word)

@tool
def calculate_trip(amount: float, percent: float) -> float:
    """ 음식점 영수증 금액과 팁 비율(%)을 입력받아서 팁 금액을 계산한다.
        인자값:
            amount: 음식 가격 (원)
            percent: 팁 비율 (%)
        예시:
            10000원에 10% 팁은 = 1000원
    """

    return amount * percent / 100

@tool
def search_user(user_id: str) -> dict:
    """ 사용자 ID로 사용자 정보를 조회한다. 존재하지 않으면 {} 빈 dict를 반환한다.
    """

    db = {
        "u001": {"name": "홍길동", "city": "서울", "age": 30},
        "u002": {"name": "김철수", "city": "부산", "age": 20},
    }
    return db.get(user_id, {})

tools = [get_word_length, calculate_trip, search_user]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)

print("=== 툴 상태 확인 ===")
for t in tools:
    print(f"[Tool] {t.name}")
    print(f"설명 : {t.description}")
    print(f"인자 스키마 : {t.args_schema.model_json_schema()}")

print("\n\n=== 툴 호출 ===")

questions = [
    "this-is-a-long-sentence 문장에 글자는 몇개야?",
    "5만원 영수증에 15$ 팁을 주려면",
    "홍길동 사용자 정보는?",
    "u001 사용자 정보는?"
]

name2tool = {t.name: t for t in tools}

for q in questions:
    r = llm_with_tools.invoke(q)
    print(f"[질문] {q}")
    for call in r.tool_calls:
        print(f" -> {call['name']} ({call['args']})")

        result = name2tool[call['name']].invoke(call['args'])   # 실행
        print(f" -> 결과: {result}")

"""
=== 툴 상태 확인 ===
[Tool] get_word_length
설명 : 단어를 글자 수를 세어서 숫자로 변환한다
인자 스키마 : {'description': '단어를 글자 수를 세어서 숫자로 변환한다 ', 'properties': {'word': {'title': 'Word', 'type': 'string'}}, 'required': ['word'], 'title': 'get_word_length', 'type': 'object'}
[Tool] calculate_trip
설명 : 음식점 영수증 금액과 팁 비율(%)을 입력받아서 팁 금액을 계산한다.
       인자값:
           amount: 음식 가격 (원)
           percent: 팁 비율 (%)
       예시:
           10000원에 10% 팁은 = 1000원
인자 스키마 : {'description': '음식점 영수증 금액과 팁 비율(%)을 입력받아서 팁 금액을 계산한다.\n인자값:\n    amount: 음식 가격 (원)\n    percent: 팁 비율 (%)\n예시:\n    10000원에 10% 팁은 = 1000원', 'properties': {'amount': {'title': 'Amount', 'type': 'number'}, 'percent': {'title': 'Percent', 'type': 'number'}}, 'required': ['amount', 'percent'], 'title': 'calculate_trip', 'type': 'object'}
[Tool] search_user
설명 : 사용자 ID로 사용자 정보를 조회한다. 존재하지 않으면 {} 빈 dict를 반환한다.
인자 스키마 : {'description': '사용자 ID로 사용자 정보를 조회한다. 존재하지 않으면 {} 빈 dict를 반환한다.', 'properties': {'user_id': {'title': 'User Id', 'type': 'string'}}, 'required': ['user_id'], 'title': 'search_user', 'type': 'object'}


=== 툴 호출 ===
[질문] this-is-a-long-sentence 문장에 글자는 몇개야?
 -> get_word_length ({'word': 'this-is-a-long-sentence'})
 -> 결과: 23
[질문] 5만원 영수증에 15$ 팁을 주려면
 -> calculate_trip ({'amount': 50000, 'percent': 15})
 -> 결과: 7500.0
[질문] 홍길동 사용자 정보는?
 -> search_user ({'user_id': '홍길동'})
 -> 결과: {}
[질문] u001 사용자 정보는?
 -> search_user ({'user_id': 'u001'})
 -> 결과: {'name': '홍길동', 'city': '서울', 'age': 30}
"""