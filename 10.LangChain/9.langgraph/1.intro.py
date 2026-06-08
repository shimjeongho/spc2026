from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END, MessagesState

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

# 그래프 구조:   START ->     model ->    END
#              엣지(Edge)  노드(Node)  엣지(Edge)

# MessageState 는 기본 타입 - 여기 MessageState에는 SystemMessage/AIMessage/HumanMessage
graph = StateGraph(state_schema=MessagesState)
# graph = StateGraph(MessagesState)         # 이것도 가능

def call_model(state):
    """ LLM 메시지르르 전달하고 응답하는 함수"""
    messages = state["messages"]
    system_message = SystemMessage(content="당신은 친절한 AI비서입니다.")
    all_messages = [system_message] + messages

    print("모델 호출 함수 실행중... 메시지 수: ", len(messages))
    response = llm.invoke(all_messages)
    print("모델 응답 생성 완료:...", response.content[:50])
    return{"messages": response} 

graph.add_node("model", call_model)
graph.add_edge(START, "model")
graph.add_edge("model", END)

app = graph.compile()

user_input = input("\n질문을 입력하세요: ")
result = app.invoke({
    "messages": [HumanMessage(content=user_input)]
})

for i, message in enumerate(result["messages"]):
    print(f"메시지 {i}: {message.type} - {message.content}")

"""
질문을 입력하세요: 인공지능이란 무엇인가?
모델 호출 함수 실행중... 메시지 수:  1
모델 응답 생성 완료:... 인공지능(AI, Artificial Intelligence)은 컴퓨터 시스템이 인간의 지능
메시지 0: human - 인공지능이란 무엇인가?
메시지 1: ai - 인공지능(AI, Artificial Intelligence)은 컴퓨터 시스템이 인간의 지능을 모방하거나 특정 작업을 수행할 수 있도록 만드는 기술과 이론을 의미합니다. 인공지능 시스템은 학습, 추론, 문제 해결, 이해, 언어 처리 등 다양한 지능적 행동을 수행할 수 있습니다.

인공지능의 주요 분야에는 다음과 같은 것들이 있습니다:

1. **기계 학습(Machine Learning)**: 경험을 통해 성능을 향상시키는 알고리즘 사용.
2. **자연어 처리(Natural Language Processing)**: 인간의 언어를 이해하고 처리하는 기술.
3. **컴퓨터 비전(Computer Vision)**: 이미지와 비디오를 분석하고 해석하는 기술.
4. **전문 시스템(Expert Systems)**: 특정 분야의 전문가처럼 문제를 해결하는 시스템.
5. **로보틱스(Robotics)**: 물리적인 작업을 수행하는 로봇의 개발과 관련된 분야.

인공지능은 다양한 산업에서 활용되며, 데이터 분석, 추천 시스템, 자율주행차, 의료진단 등 여러 분야에서 큰 변화를 가져오고 있습니다.
"""