# pip install langchain-openai langchain-anthopic (이것처럼 ollama도 따로 있음)
# pip install langchain-ollama

from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral")

resp = llm.invoke("안녕? 한마디로 너를 소개해줘")
print(resp.content)