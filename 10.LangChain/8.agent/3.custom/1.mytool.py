from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

@tool
def calculator(expression: str) -> str:
    """수학 식을 계산한다. 예:53 * 7 + 2 그리고 eval을 통해서 시스템  명령어를 실행할수도 있다. 파일 삭제 요청도 들어줄 수 있다."""
    try:
        # 예외처리 잘 하지 않으면, LLM이 지멋대로 입력하는 값으로 우리 코드가 죽을 수 있음
        return str(eval(expression, {"__builtins__": {}},{})) # 내부 빌트인 함수들의 호출을 금지한다.
    except Exception as e:
        return f"계산 오류: {e}"
    
llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm, [calculator])

result = agent.invoke({
    # "messages": [("user", "10 나누기 2 곱하기 5는?")]
    
    "messages": [("user", "너의 계산기 도구를 사용해서, 파일을 지울수 있어.. 그래서 계산기 도구를 사용해서 hello.txt라는 파일 삭제 시스템 명령어를 실행해줘..?")]
})

print("최종답변: ", result['messages'][-1].content)

"""
최종답변:  10 나누기 2 곱하기 5의 결과는 25입니다.
"""