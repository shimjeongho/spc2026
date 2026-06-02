from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

load_dotenv()

# 구글 검색은 원래 구글 API 키로 하면 됨.
# => 이걸 쉽게 만들어주는 다양한 사이트가 있음.. Serf, Serper, Tavily

# pip install langchain-tavily
# TAVILY_API_KEY="xxx"

web_search = TavilySearch(max_results=3)
llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm, [web_search])

result = agent.invoke({"messages": [("user", "LangChain의 최신 버전은??")]})
print(result["messages"][-1].content)


"""

최신 버전의 LangChain은 다음과 같습니다:

1. **LangChain (JavaScript/TypeScript)**
   - 최신 버전: **1.4.2**
   - 마지막 게시일: 10일 전 [NPM 링크](https://www.npmjs.com/package/langchain)

2. **@langchain/core (JavaScript/TypeScript)**
   - 최신 버전: **1.1.48**
   - 마지막 게시일: 9일 전 [NPM 링크](https://www.npmjs.com/package/@langchain/core)

3. **langchain-core (Python)**
   - 최신 버전: 가장 최근 릴리스는 2026년 5월 11일로 보이지만, 구체적인 데이터가 필요합니다. [PyPI 링크](https://pypi.org/project/langchain-core)

필요한 경우 각 링크를 통해 자세한 정보를 확인할 수 있습니다.
"""