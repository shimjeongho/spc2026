from dotenv import load_dotenv

# 프롬프트
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 모델
from langchain_openai import ChatOpenAI
# 파서
from langchain_core.output_parsers import StrOutputParser
# 기타
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini") 

prompt = ChatPromptTemplate.from_messages ([
    ("system", "당신은 친절한 챗봇입니다."), 
    MessagesPlaceholder("history"),
    ("user", "{input}"),
])

chain = prompt | llm | StrOutputParser()

# 파일에 저장하는 형식이 아니라 서버 끝면 기억 못함
history = InMemoryChatMessageHistory()

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
질문: 안녕하세요
답변: 안녕하세요! 어떻게 도와드릴까요?
질문: 제 이름은 곽길동 입니다.
답변: 안녕하세요, 곽길동님! 만나서 반갑습니다. 어떻게 도와드릴까요?
질문: 저는 겨울에 바닷가에 가서 서핑하는것을 좋아합니다.
답변: 겨울에 바닷가에서 서핑을 즐기는 것은 정말 멋진 경험이겠네요! 바다의 파도를 타는 기분은 어떤가요? 그리고 어떤 해변을 자주 가시나요?
질문: 제 이름과 취미가 뭐라고 했죠??
답변: 당신의 이름은 곽길동님이고, 겨울에 바닷가에서 서핑하는 것을 좋아한다고 하셨어요. 맞나요?
"""