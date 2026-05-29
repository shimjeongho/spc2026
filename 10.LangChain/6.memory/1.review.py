from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini") 

prompt = ChatPromptTemplate.from_messages ([
    ("system", "당신은 친절한 챗봇입니다."),  # 나의 페르소나  (system)
    ("user", "{input}")                     # 나의 질문  (user), (human)
    # ("ai", "챗봇 답변")                      # 챗봇 답변  (ai), (assistant)
    # ("user", "{input}")                      # 나의 질문
])

chain = prompt | llm | StrOutputParser()
print(chain.invoke({"input": "안녕하세요, 나는 홍길동 입니다."}))
print(chain.invoke({"input": "그래서, 내가 누구라구요?"}))
print(chain.invoke({"input": "방금 말했는데, 모르시네요"}))

"""
안녕하세요, 홍길동님! 만나서 반갑습니다. 어떻게 도와드릴까요?
죄송하지만, 저는 개인적인 정보를 알 수 없습니다. 하지만 당신이 어떤 질문이든 하거나 이야기하고 싶은 것이 있다면 도와드릴 수 있습니다! 무엇에 대해 이야기하고 싶으신가요?
죄송합니다. 제가 놓친 부분이 있을 수도 있습니다. 어떤 내용을 말씀하셨는지 다시 한번 말씀해 주시면, 최선을 다해 도와드리겠습니다!
"""

print('-' * 60)

prompt_with_history = ChatPromptTemplate.from_messages ([
    ("system", "당신은 친절한 챗봇입니다."),  # 나의 페르소나  (system)
    MessagesPlaceholder("history"),     # <- 여기 공간에 우리의 대화내용을 넣으려고 하는것
    ("user", "{input}")
])

chain2 = prompt_with_history | llm | StrOutputParser()

history_example = [
    HumanMessage(content="안녕하세요, 저는 홍길동입니다."),
    AIMessage(content="네, 홍길동님 반갑습니다.")
]

answer = chain2.invoke({
    "history": history_example,
    "input": "제 이름이 뭐였죠?"
})

print(answer)
