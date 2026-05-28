# 목적: 다양한 목적에 맞는 이메일을 작성해준다.

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate
)

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    "당신은 기업의 커뮤니케이션 전문가입니다."
    "포멀하게 전문가 톤으로 이메일을 작성하시오."),
    HumanMessagePromptTemplate.from_template(
        "수신자 '{recipient}' 에게 다음 주제 '{topic}' 에 대한 미팅 요청을 하는 메일을 작성하시오"
    )
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=1000)

chain = chat_prompt | llm | StrOutputParser()

# 다양한 수신자와 다양한 주제
recipients = [
    "마케팅팀",
    "개발팀",
    "영업팀",
    "인사팀"
]
topics = [
    "신제품 출시 전략",
    "분기별 개발 성과 지표",
    "개인별 매출 목표차 달성 현황 리뷰",
    "개발을 잘 못해서 맨날 버그만 발생시키는 개발자 해고"
]

for recipient, topic in zip(recipients, topics):
    print('-----')
    print(f"To: {recipient}, Topic: {topic}")
    print('-----')
    result = chain.invoke({"recipient": recipients[0], "topic": topics[0]})
    print(result)
    print('-----')

"""
-----
To: 마케팅팀, Topic: 신제품 출시 전략
-----
제목: 신제품 출시 전략 관련 미팅 요청

안녕하세요, 마케팅팀 여러분.

저희는 오는 [날짜]에 신제품 출시와 관련된 전략 수립을 위한 미팅을 개최하고자 합니다. 이번 미팅은 신제품의 시장 진입 전략, 프로모션 계획 및 타겟 고객 분석 등을 논의하는 중요한 자리로, 모든 팀원 여러분의 소중한 의견이 필요합니다.

미팅 일정은 다음과 같습니다:

- 일시: [날짜 및 시간]
- 장소: [장소 또는 온라인 회의 링크]
- 안건: 신제품 출시 전략 수립

미팅에 참여 가능하신지 확인해 주시기 바라며, 추가 논의하고 싶은 사항이 있으시면 미리 말씀해 주시면 감사하겠습니다.

여러분의 적극적인 참여를 부탁드립니다.

감사합니다.

[당신의 이름]  
[당신의 직책]  
[회사 이름]  
[연락처]  
-----
-----
To: 개발팀, Topic: 분기별 개발 성과 지표
-----
제목: 신제품 출시 전략 관련 미팅 요청

안녕하세요, 마케팅팀 여러분.

저희가 계획 중인 신제품 출시와 관련하여 전략적인 논의를 진행하고자 합니다. 이에 따라 다음 주 중에 미팅을 요청드립니다. 이번 미팅에서는 제품의 시장 진입 전략, 타겟 고객층, 마케팅 캠페인 및 출시 일정 등에 대해 심도 있는 논의가 필요할 것으로 생각됩니다.

가능한 일정에 대해 알려주시면, 팀원들의 편리한 시간에 맞추어 회의를 조율하도록 하겠습니다. 모든 팀원들의 참여를 통해 보다 효과적인 출시 전략을 수립할 수 있기를 기대합니다.

감사합니다.

[귀하의 이름]  
[귀하의 직책]  
[귀하의 연락처]  
[회사명]
-----
-----
To: 영업팀, Topic: 개인별 매출 목표차 달성 현황 리뷰
-----
제목: 신제품 출시 전략 관련 미팅 요청

안녕하세요, 마케팅팀 여러분.

저희는 다가오는 신제품 출시를 준비하고 있으며, 이에 대한 효과적인 전략 수립이 필요하다고 판단하고 있습니다. 따라서, 신제품 출시 전략에 대한 논의를 위한 미팅을 요청 드립니다.

미팅의 주요 안건은 다음과 같습니다:
1. 시장 분석 및 목표 설정
2. 브랜드 포지셔닝 전략
3. 마케팅 캠페인 계획
4. 타겟 고객층 정의

가능한 날짜와 시간을 알려주시면, 조율하여 미팅 일정을 확정하겠습니다. 모든 팀원들의 소중한 의견이 반영될 수 있도록 적극적인 참여를 부탁드립니다.

감사합니다.

[당신의 이름]  
[당신의 직책]  
[회사명]  
[연락처]  
-----
-----
To: 인사팀, Topic: 개발을 잘 못해서 맨날 버그만 발생시키는 개발자 해고
-----
제목: 신제품 출시 전략 미팅 요청

안녕하세요, 마케팅팀 여러분.

저희는 곧 출시될 신제품에 대한 전략을 논의하기 위해 미팅을 요청하고자 합니다. 제품의 성공적인 론칭을 위해 각 부서의 의견과 아이디어가 매우 중요하다고 생각합니다.

미팅은 다음 주 중으로 진행하고자 하며, 여러분의 편리한 일정을 고려하여 시간 조정을 하고자 합니다. 가능한 날짜와 시간을 알려주시면 감사하겠습니다.

이번 미팅에서는 다음과 같은 주요 사항들을 다룰 예정입니다:

1. 신제품의 주요 특징 및 타겟 시장
2. 마케팅 및 홍보 전략
3. 출시 일정 및 예산 계획
4. 기타 협업 사항

여러분의 많은 참여와 적극적인 의견 개진을 부탁드립니다. 신제품 출시가 성공적으로 이루어질 수 있도록 함께 힘을 모아주시면 감사하겠습니다.

감사합니다.

[당신의 이름]  
[당신의 직책]  
[회사명]  
[연락처]  
[이메일 주소]  
-----
"""