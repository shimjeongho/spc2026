from dotenv import load_dotenv

# 프롬프트
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 모델
from langchain_openai import ChatOpenAI
# 파서
from langchain_core.output_parsers import StrOutputParser

# 기타
from langchain_community.chat_message_histories import SQLChatMessageHistory
# sql 파일 잘 관리해줌
from sqlalchemy import create_engine

load_dotenv()

DB_URL = "sqlite:///chat_history.db"
SESSION_ID = "default"  # 나중에 사용자별로 이걸 바꿔주면됨

engine = create_engine(DB_URL)
history = SQLChatMessageHistory(session_id=SESSION_ID, connection=engine)

llm = ChatOpenAI(model="gpt-4o-mini") 

prompt = ChatPromptTemplate.from_messages ([
    ("system", "당신은 친절한 챗봇입니다."), 
    MessagesPlaceholder("history"),
    ("user", "{input}"),
])

chain = prompt | llm | StrOutputParser()


def chat(message):
    print(f"질문: {message}")
    answer = chain.invoke({
        "input": message,
        # "history": history.messages,       # 우리의 저장소에 있는 메시지 그대로 다
        "history": history.messages[-10:],  # 최근 10개 대화만 가져온다.
    })
    print(f"답변: {answer}")
    history.add_user_message(message)
    history.add_ai_message(answer)

chat("안녕하세요")
chat("제 이름은 곽길동 입니다.")
chat("저는 겨울에 바닷가에 가서 서핑하는것을 좋아합니다.")
chat("제 이름과 취미가 뭐라고 했죠??")

"""
### chat_history.db에 들어감

질문: 안녕하세요
답변: 안녕하세요! 어떻게 도와드릴까요?
질문: 제 이름은 곽길동 입니다.
답변: 곽길동님, 만나서 반갑습니다! 어떤 이야기를 나눠볼까요?
질문: 저는 겨울에 바닷가에 가서 서핑하는것을 좋아합니다.
답변: 겨울에 바닷가에서 서핑하는 것은 정말 멋진 경험일 것 같네요! 차가운 바다와 시원한 공기 속에서 서핑을 즐기는 것은 색다른 매력이 있죠. 서핑을 하면서 특별한 추억이나 즐거운 경험이 있으셨나요?
질문: 제 이름과 취미가 뭐라고 했죠??
답변: 곽길동님이라고 하셨고, 겨울에 바닷가에서 서핑하는 것을 좋아하신다고 말씀하셨습니다. 맞나요? 더 이야기하고 싶은 내용이나 질문이 있으신가요?
"""