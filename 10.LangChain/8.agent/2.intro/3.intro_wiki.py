# pip install wikipedia

import wikipedia
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_agent # 이 함수는 3번이상 바뀜

load_dotenv()

tools = load_tools(["wikipedia"])

llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm, tools)

result = agent.invoke({"messages": [("user", "파이썬 프로그래밍 언어는 누가 만들었을까?")]})
print(result)