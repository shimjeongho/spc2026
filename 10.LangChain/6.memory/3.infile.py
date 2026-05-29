# pip install langchain-community
from dotenv import load_dotenv

# 프롬프트
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 모델
from langchain_openai import ChatOpenAI
# 파서
from langchain_core.output_parsers import StrOutputParser
# 기타
from langchain_community.chat_message_histories import FileChatMessageHistory

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini") 

prompt = ChatPromptTemplate.from_messages ([
    ("system", "당신은 친절한 챗봇입니다."), 
    MessagesPlaceholder("history"),
    ("user", "{input}"),
])

chain = prompt | llm | StrOutputParser()

history = FileChatMessageHistory("history.json")

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
### history.json에 저장
#  
질문: 안녕하세요
답변: 안녕하세요! 어떻게 도와드릴까요?
질문: 제 이름은 곽길동 입니다.
답변: 반갑습니다, 곽길동님! 무엇을 도와드릴까요?
질문: 저는 겨울에 바닷가에 가서 서핑하는것을 좋아합니다.
답변: 겨울에 바닷가에서 서핑하다니 정말 멋진 취미네요! 겨울 바다에서의 서핑은 다른 계절과 또 다른 매력이 있을 것 같아요. 서핑을 하면서 어떤 경험이 가장 기억에 남았나요?
질문: 제 이름과 취미가 뭐라고 했죠??
답변: 곽길동님, 겨울에 바닷가에 가서 서핑하는 것을 좋아한다고 말씀하셨습니다! 맞나요? 혹시 더 이야기하고 싶은 내용이 있으신가요?
"""