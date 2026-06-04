from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

technical_prompt = ChatPromptTemplate.from_template(
"""
    당신은 기술직원 전문가입니다. 정확하고 단계별로 문제를 해결하는 방법을 안내해주세요.

    고객문의:
    {question}

    기술 지원 응답:


"""
)
technical_chain = technical_prompt | llm | parser

billing_prompt = ChatPromptTemplate.from_template(
    # 고객이 환불 또는 회원탈퇴를 원할 경우, 정중하게 사과를 하고, 다른 상품 구래를 유도해주세요
"""
당신은 결제 및 구독 전문 상답원입니다. 사내 정책에 따라 안내하고, 친절하게 응대해주세요

고객문의:
{question}

결제 지원 응답:

"""
)
billing_chain = billing_prompt | llm | parser

general_prompt = ChatPromptTemplate.from_template(
"""
당신은 친절한 고객 서비스 담당자입니다. 고객의 질문에 대해 친절하게 답변해주세요.

고객문의:
{question}

일반 응답:
"""
)

general_chain = general_prompt | llm | parser


route_map = {
    "technical": technical_chain, # 기술적인 질문에 답변하는 체인
    "billing": billing_chain, # 결제관련 질문에 답변하는 체인
    "general": general_chain # 그외 기타 나머지 일반적인 질문
}

classifier_prompt = ChatPromptTemplate.from_template(
"""
다음 고객 문의를 보고, 어느 카테고리에 해당하는지 분류해 주세요. 반드시 아래 카테고리 중 하나로만 출력해주세요.

카테고리 선택 항목: technical, billing, general

고객문의: {question}

카테고리:
"""
)
classifier_chain = classifier_prompt | llm | parser

# 사용자의 질문을 받아 적절한 챗봇으로 라우팅한다.
def route_query(input: dict) -> str:
    question = input["question"]

    # 1단계. 분류를 시켜서 카테고리를 가져온다.
    category = classifier_chain.invoke({"question": question}).strip().lower()
    print(f"분류 결과: {category}")

    # 2단계. 해당 카테고리 체인을 다시 호출한다.
    chain = route_map.get(category, general_chain)
    response = chain.invoke({"question": question})

    return f"[{category.upper()}] {response}"


routing_chain = RunnableLambda(route_query)


test_questions = [
    "프로그램이 자꾸 충돌하는데 어떻게 해야 하나요?"
    "구독을 취소하고 환불받고 싶습니다."
    "이 서비스에서는 어떤 기능을 제공하나요?"
    "API 연동 시 인증 오류가 발생합니다."
]


for i, question in enumerate(test_questions, 1):
    print(f"\n------------------")
    print(f"질문 {i}: {question}")
    result = routing_chain.invoke({"question": question})
    print(f"응답: {result}")

"""
------------------
질문 1: 프로그램이 자꾸 충돌하는데 어떻게 해야 하나요?구독을 취소하고 환불받고 싶습니다.이 서비스에서는 어떤 기능을 제공하나요?API 연동 시 인증 오류가 발생합니다.
분류 결과: technical
응답: [TECHNICAL] 안녕하세요! 고객님의 문의에 대해 단계별로 답변드리겠습니다.

### 1. 프로그램 충돌 문제 해결
   - **문제 확인**: 프로그램이 충돌하는 특정 상황(예: 특정 기능 사용 시, 프로그램 실행 중 등)이 있는지 확인합니다.
   - **업데이트 확인**: 프로그램이 최신 버전인지 확인하고, 필요시 업데이트합니다.
   - **로그 파일 확인**: 충돌 시 생성된 로그 파일을 확인하여 원인을 파악합니다.
   - **재설치**: 프로그램을 제거한 후 최신 버전을 다시 설치하여 문제가 해결되는지 확인합니다.
   - **기술 지원 요청**: 위의 방법으로 해결되지 않는 경우, 고객님의 시스템 정보와 로그 파일을 포함하여 기술 지원팀에 문의해 주세요.

### 2. 구독 취소 및 환불 요청
   - **구독 관리**: 고객님의 계정으로 로그인 후 구독 관리 섹션으로 이동합니다.
   - **취소 절차**: 구독 취소 옵션을 선택하고 화면의 지시에 따라 진행합니다.
   - **환불 요청**: 구독 취소 후, 환불 요청을 위한 양식이나 고객 지원팀에 직접 연락하여 환불 사유를 설명합니다.
   - **확인**: 환불 요청 후 이메일 등을 통해 확인 메시지를 받습니다.

### 3. 서비스 기능 안내
   - **서비스 소개**: 고객님께 제공되는 주요 기능과 서비스 목록을 정리하여 안내합니다.
   - **데모/튜토리얼**: 필요시 서비스 사용 방법에 대한 데모 영상이나 튜토리얼 링크를 제공하여 고객님이 보다 쉽게 이해할 수 있도록 합니다.
   - **자주 묻는 질문**: 추가적인 질문이 있을 경우 자주 묻는 질문(FAQ) 섹션을 안내드립니다.

### 4. API 연동 시 인증 오류 해결
   - **인증 정보 확인**: API 키, 비밀번호 등 입력한 인증 정보가 정확한지 확인합니다.
   - **서버 상태 점검**: API 제공자의 서버 상태나 장애 공지를 확인합니다.
   - **코드 검토**: API 호출 코드(예: 헤더, 요청 방식 등)를 검토하여 문제가 있는지 확인합니다.
   - **오류 메시지 분석**: 발생하는 인증 오류 메시지를 기반으로 어떤 문제인지 파악합니다.
   - **문서 참조**: API 제공자의 문서에서 인증 관련 정보를 다시 확인합니다.
   - **기술 지원 요청**: 문제가 해결되지 않는 경우, 사용 중인 API 정보와 오류 메시지를 포함하여 기술 지원팀에 문의해 주세요.

이와 같은 방식으로 각 문제에 대해 단계별로 조치를 취하시기 바랍니다. 추가적인 도움이 필요하시면 언제든지 연락 주세요!
"""