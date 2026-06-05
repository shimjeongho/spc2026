from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# ('[1단계] 리서치 수행중')
research_prompt = ChatPromptTemplate.from_template(
    "다음 주제에 대해 핵심 사실 5가지를 간결하게 정리해주세요"
    "\n\n주제: {topic}"
)
research_chain = research_prompt | llm | parser

# ('[2단계] 게이트 검증 수행중')
gate_prompt = ChatPromptTemplate.from_template(
"""
다음 리서치 결과가 적합한지 평가해 주세요.

---
리서치 결과: 
{research}

---
평가 기준:
1. 사실 5가지가 올바르게 포함되어 있는가?
2. 각 사실이 구체적이고 검증 가능한가?
3. 주제와 관련이 있는가?

---
결과:
PASS 또는 FAIL 로만 답하고, PASS인 경우 아무런 설명도 없이 PASS 만, 실패인 경우 이유를 한줄로 설명하시오.
"""
)

gate_chain = gate_prompt | llm | parser


# ('[3단계] 분석 수행중')
analysis_prompt = ChatPromptTemplate.from_template(
"""
다음 리서치 결과를 바탕으로 심층 분석 내용을 적상해주시오.

---
리서치 결과: 
{research}

---
다음을 포함해주세요:
- 핵심 트랜드 또는 패턴
- 시사점
- 향후 전장
"""
)

analysis_chain = gate_prompt | llm | parser


# ('[4단계] 보고서생성 수행중')
report_prompt = ChatPromptTemplate.from_template(
# (CEO에게 보고를 위한, 실무자가 팀장에게 보고하는 형태의, 등등 다양하게 바꿔볼것, 초등학생도 이해할수 있도록 쉬운 레벨로)
"""
다음 리서치와 분석 된 내용을 바탕으로 간결한 CEO에게 보고를 위한 보고서를 작성하시오.

---
리서치: 
{research}

---
분석: 
{analysis}

---
출력형식:
- 제목
- 요약 (3줄)
- 핵심 발견사항
- 결론
"""
# - 기본 디자인을 포함한 HTML 단일 파일 파일 문서로 CSS까지 포함
)

report_chain = report_prompt | llm | parser


def run_chaining_pipeline(topic):
    # 1단계: 리서치
    print('[1단계] 리서치 수행중')
    research = research_chain.invoke({'topic': topic})

    # 2단계: 게이트 검증
    print('[2단계] 게이트 검증 수행중')
    gate_result = gate_chain.invoke({'research': research})
    print("2단계 결과: ", gate_result)
    if gate_result.lower() in "fail":
        print("게인트 검증에 실패하여 해당 업무를 재수행 합니다.")
        gate_result = gate_chain.invoke({'research': research})
        # 고도화를 할거면, 반복 횟수 정의하거나, 프롬프트를 살짝씩 고도화 한거로 시키거나, 또는 모델(gpt-4o-mini) 대신 일 더 잘하는 애를 고용하거나 한다.

    # 3단계: 분석 수행
    print('[3단계] 분석 수행중')
    analysis = analysis_chain.invoke({'research': research})

    # 4단계: 보고서 생성
    print('[4단계] 보고서생성 수행중')
    report = report_chain.invoke({'research': research, 'analysis': analysis})

    return report


# 질문
# 1. 2026년도 생성형 AI 시장 동향 조사를 해오시오.
# topic = "2026년도 생성형 AI 시장 동향 조사를 해오시오."
topic = "2025년도의 한해동안의 주요 해킹 사례와 보안 기술 동향을 조사해줘"

result = run_chaining_pipeline(topic)
print('-' * 60)
print('최종 보고서:')
print('-' * 60)

# 리서치 -> 분석 -> 보고서
print(result)

"""
[1단계] 리서치 수행중
[2단계] 게이트 검증 수행중
2단계 결과:  PASS
[3단계] 분석 수행중
[4단계] 보고서생성 수행중
------------------------------------------------------------
최종 보고서:
------------------------------------------------------------
### 2025년도 해킹 사례 및 보안 기술 동향 보고서

#### 요약
2025년에는 고급 지속 위협(APT) 공격, 진화하는 랜섬웨어, IoT 보안 취약점의 증가, AI 기반 보안 솔루션의 발전, 그리고 사이버 보안 규제의 강화가 두드러졌습니다. 이러한 요인은 기업과 기관에 심각한 위협을 초래하고 있습니다. 이에 따라, 효과적인 보안 대응 전략이 필수적입니다.

#### 핵심 발견사항
1. **고급 지속 위협(APT)**: 국가 지원 해킹 그룹의 증가로 특정 산업을 겨냥한 공격이 빈번하게 발생하고 있습니다.
2. **랜섬웨어의 진화**: 복잡한 비즈니스 모델로 진화하면서, '랜섬웨어-as-a-Service' 형태의 협업 공격이 일반화되었습니다.
3. **IoT 보안 취약점**: IoT 기기의 보급이 확산됨에 따라 해킹 사례가 급증하고, 이는 botnet 구축에 악용되고 있습니다.
4. **AI 기반 보안 솔루션 강화**: 머신러닝과 AI 기술이 보안 솔루션에 적용되어 실시간 위협 탐지 및 대응 능력이 향상되었습니다.
5. **규제 강화**: 사이버 보안 관련 규제가 강화되며, 해킹 사건의 공개적인 보고가 의무화되어 투명성이 높아졌습니다.

#### 결론
2025년도 해킹 사례와 보안 기술의 동향은 기업과 정부 기관에게 새로운 보안 과제를 제기하고 있습니다. 예방 및 탐지를 위한 AI 기반 솔루션의 도입과 함께, 사이버 보안 규제 준수가 중요합니다. 즉각적인 보안 전략을 마련하고, 지속적인 모니터링을 통해 피해를 최소화하는 것이 필요합니다.
"""