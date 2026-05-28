from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

prompt_name = ChatPromptTemplate.from_template(
    "{product} 을 만드는 회사의 이름을 하나 추천해주세요. 이름만 답하시오."
)
prompt_slogan = ChatPromptTemplate.from_template(
    "{company_name} 회사의 캐치프레이즈를 만들어주세요. 캐치프레이즈만 답하시오."
)

chain2 = (
    # 사용자 입력 처리
    prompt_name 
    | llm 
    | StrOutputParser() 
    | RunnableLambda(lambda name: {"company_name": name.strip()}) 

    # 두번째 체인
    | RunnableLambda(lambda d: {
        "company_name": d["company_name"],
        "slogan": (
            prompt_slogan
            | llm
            | StrOutputParser()
        ).invoke({
            "company_name": d["company_name"]
        })
    })
   
)

# result = chain1.invoke({"product": "친환경 에코백"})
result1 = chain2.invoke({"product": "친환경 에코백"})
print(f"결과: {result1}")

"""
# result1 = chain2.invoke({"product": "친환경 에코백"})
결과: {'company_name': '에코손길', 'slogan': '"지구를 향한 한 걸음, 에코손길과 함께!"'}
"""
# 입력 -> 회사명작명 -> 슬로건작성 -> 출력
# 한국어입력 -> 영어입력 -> 중국어번역 -> 일본어번역 -> 출력
# 한국어입력 -> 영어 번역 -> 출력  (동시 처리)
#           -> 중국어번역
#           -> 일본어번역