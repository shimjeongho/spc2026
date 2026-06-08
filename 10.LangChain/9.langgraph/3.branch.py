import uuid

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.runnables import RunnableConfig

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

from typing import TypedDict, List, Dict, Any

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
memory = MemorySaver()

#              엣지(Edge)  노드(Node)  엣지(Edge)
# 그래프 구조:   START ->     model ->    END
#                              ^
#                            메모리

def get_weather():
    print("가상의 날씨 반환중...")
    return "오늘 서울의 날씨는 맑고 기온이 22도 입니다."

"""
질문을 입력하세요: 날씨는?
라우터: '날씨'를 감지하여 weather 라우팅으로 보내는중...
가상의 날씨 반환중...
AI 선택토픽: weather, 응답: 안녕하세요! 오늘 서울의 날씨는 아주 맑고 기분 좋은 날씨입니다. 현재 기온은 22도라서 외출하기에 적당한 온도입니다. 가벼운 옷차림으로 산책이나 외부 활동을 즐기기에 좋을 것 같아요. 맑은 하늘 아래에서 좋은 시간 보내시길 바랍니다!
"""

def get_news():
    return "최신 뉴스: 오늘 삼성전자 주가는 -9% 하락중입니다."

"""
질문을 입력하세요: 오늘 뉴스는?
라우터: '뉴스'를 감지하여 news 라우팅으로 보내는중...
AI 선택토픽: news, 응답: 안녕하세요! 오늘 삼성전자의 주가가 약 9% 하락한 소식이 전해졌습니다. 주가는 기업의 가치를 반영하는 중요한 지표인데, 이처럼 큰 하락은 투자자들에게 우려를 낳을 수 있습니다. 

주가 하락의 이유는 다양할 수 있는데, 예를 들어, 경제 전반의 불안정, 특정 산업 트렌드, 또는 삼성전자의 실적 발표 등이 영향을 미칠 수 있습니다. 이와 같은 변동성은 주식시장에서는 자주 발생하는 현상이며, 투자자들은 이를 바탕으로 매수 또는 매도 결정을 하게 됩니다.

혹시 이와 관련해 더 궁금한 점이 있으시면 언제든지 질문해 주세요!
"""

class State(TypedDict):
    messages: List[AIMessage]
    topic: str


def topic_router(state: State, config: RunnableConfig) -> str:
    """ 사용자 질문에 따라서 경로를 라우팅하는 함수 """
    last_message = state["messages"][-1].content.lower()    # News, news, NEWS
    if "날씨" in last_message:
        print("라우터: '날씨'를 감지하여 weather 라우팅으로 보내는중...")
        return "weather"
    if "뉴스" in last_message:
        print("라우터: '뉴스'를 감지하여 news 라우팅으로 보내는중...")
        return "news"
    print("라우터: 일반 대화 감지 chat 노드로 라우팅...")
    return "chat"

def router_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    # 특별히 할일 없음. 그냥 placeholder로만의 역할을 함.
    return {}

def weather_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    weather_info = get_weather()
    response = llm.invoke([
        SystemMessage(content="당신은 날씨 전문가 입니다."),
        HumanMessage(content=f"다음 날씨 정보를 사용자에게 친절하게 설명해주세요: {weather_info}")
    ])

    return {"messages": state["messages"] + [response], "topic": "weather"}

def news_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    news_info = get_news()
    response = llm.invoke([
        SystemMessage(content="당신은 뉴스 전문가 입니다."),
        HumanMessage(content=f"다음 뉴스 정보를 사용자에게 친절하게 설명해주세요: {news_info}")
    ])
    return {"messages": state["messages"] + [response], "topic": "news"}

def chat_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    messages = state['messages']
    response = llm.invoke([
        SystemMessage(content="당신은 친절한 AI비서 입니다.."),
        HumanMessage(content=f"{messages}")
    ])
    return {"messages": state["messages"] + [response], "topic": "chat"}

graph = StateGraph(State)
graph.add_node("router", router_node)
graph.add_node("weather", weather_node)
graph.add_node("news", news_node)
graph.add_node("chat", chat_node)

graph.add_edge(START, "router")
graph.add_conditional_edges("router",
                            topic_router, 
                            path_map={
                                "weather": "weather",
                                "news": "news",
                                "chat": "chat"
                                })

graph.add_edge("weather", END)
graph.add_edge("news", END)
graph.add_edge("chat", END)

app = graph.compile(checkpointer=memory)
thread_id = str(uuid.uuid4())
config = {"configurable": {'thread_id': thread_id}}

while True:
    user_input = input("질문을 입력하세요: ")
    if user_input.lower() == 'exit':
        break

    result = app.invoke({"messages": [HumanMessage(content=user_input)], "topic": ""}, config=config)
    print(f"AI 선택토픽: {result['topic']}, 응답: {result['messages'][-1].content}")

"""
라우터: '날씨'를 감지하여 weather 라우팅으로 보내는중...
AI 선택토픽: weather, 응답: 안녕하세요! 오늘 서울의 날씨는 아주 맑고 화창합니다. 기온은 22도로, 따뜻한 날씨가 느껴지네요. 밖에 나가시기에 정말 좋은 날이니, 가벼운 옷차림을 하시고 산책이나 소풍을 즐기셔도 좋을 것 같습니다. 햇살도 좋고 기분 전환하기에 안성맞춤인 날이에요! 외출하시기 전에 꼭 즐거운 시간을 보내세요!
질문을 입력하세요: 오늘 뉴스 좀
라우터: '뉴스'를 감지하여 news 라우팅으로 보내는중...
AI 선택토픽: news, 응답: 안녕하세요! 오늘 삼성전자 주가가 약 9% 하락하고 있다는 소식이 전해졌습니다. 주가 하락은 다양한 요인에 의해 발생할 수 있습니다. 예를 들어, 시장의 일반적인 분위기, 기업의 실적 발표, 글로벌 경제 상황, 경쟁사의 변화 등 여러 가지 이유가 있을 수 있습니다.

주식 시장에서 주가는 수요와 공급에 따라 변화하는데, 오늘 삼성전자의 경우 많은 투자자들이 주식을 매도하고 있다는 뜻일 수 있습니다. 이러한 하락은 단기적인 현상일 수도 있고, 더 긴 기간에 걸쳐 영향을 미칠 수도 있습니다.

주가가 하락하면 투자자들에게는 우려의 원인이 될 수 있지만, 전문가들은 이런 변동성을 주의 깊게 관찰하고 장기적인 투자 전략을 세우는 것이 중요하다고 말합니다. 삼성전자는 세계적으로 영향력 있는 기술 기업이므로, 시장 상황이 어떻게 변화하는지 계속 살펴보는 것이 좋겠습니다. 궁금한 점이 있으시면 언제든지 말씀해 주세요!
"""