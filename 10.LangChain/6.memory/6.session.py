from dotenv import load_dotenv
# 프롬프트
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 모델
from langchain_openai import ChatOpenAI
# 파서
from langchain_core.output_parsers import StrOutputParser
# 기타
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini") 

prompt = ChatPromptTemplate([
    ("system", "당신은 친절한 한국어 어시스턴트 입니다."),
    MessagesPlaceholder("history"),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()

# 세션관리를 위한 자료구조

# 원래는 이거였음
# sessions = {}


sessions: dict[str, InMemoryChatMessageHistory] = {}

# def get_session_history(session_id):
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in sessions:
        sessions[session_id] = InMemoryChatMessageHistory()
    return sessions[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# def chat(message):
def chat(message, session_id):
    print(f"\n[{session_id}]")
    answer = chain_with_memory.invoke(
        {"input":message},
        config={"configurable": {"session_id": session_id}},        # *** 여기가 세션관리의 핵심 ***
    )
    print(f"[{session_id}] 답변: {answer}")

user_a = "user-A" # 세션 ID 임의 생성
user_b = "user-B" # 세션 ID 임의 생성

chat("제 이름은 홍길동 입니다.", user_a)
chat("제 이름은 김철수 입니다.", user_b)
chat("저는 등산을 좋아합니다.", user_a)
chat("저의 취미는 낚시 입니다.", user_b)
chat("저는 누구인가요??", user_a)
chat("저는 누구인가요??", user_b)

"""
[user-A]
[user-A] 답변: 안녕하세요, 홍길동 씨! 만나서 반갑습니다. 어떻게 도와드릴까요?

[user-B]
[user-B] 답변: 안녕하세요, 김철수님! 만나서 반갑습니다. 어떻게 도와드릴까요?

[user-A]
[user-A] 답변: 등산을 좋아하시군요! 자연 속에서 시간을 보내는 것은 정말 기분이 좋죠. 가장 좋아하는 등산 코스가 있으신가요? 아니면 추천하고 싶은 산이 있으신가요?

[user-B]
[user-B] 답변: 낚시는 정말 재밌는 취미죠! 어떤 종류의 낚시를 좋아하시나요? 바다 낚시, 민물 낚시, 혹은 다른 종류의 낚시를 즐기시나요?

[user-A]
[user-A] 답변: 홍길동 씨는 등산을 좋아하는 분이십니다! 더 궁금하신 점이나 자신에 대해 더 이야기하고 싶은 내용이 있으신가요? 기꺼이 도와드리겠습니다!

[user-B]
[user-B] 답변: 김철수님은 낚시를 취미로 가지신 분이신 것 같아요. 혹시 더 알고 싶은 내용을 말씀해 주시면 좋을 것 같습니다. 어떤 질문이든지 도와드릴게요!
"""