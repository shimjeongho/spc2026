# 1. 프롬프트 생성
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 브랜드 기획자 입니다."),
    ("user", "회사의 홍보하기 위한 캐치프레이즈을 5개 만들어줘."
             "회사명: {company} 상품명: {product}"
             "출력 결과는 콤마로 구분된 리스트 (CSV)로 만들어줘."
    )
])

filled_prompt = prompt.format_messages(company="테슬라", product="Model S")

# 2. LLM 모델 호출
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke(filled_prompt)
print(response.content)

# 3. 출력 파서 (Output Parser)
from langchain_core.output_parsers import StrOutputParser # String 파서
from langchain_core.output_parsers import CommaSeparatedListOutputParser # CSV 파서

parser1 = StrOutputParser()
parser2 = CommaSeparatedListOutputParser()

result_str = parser1.invoke(response)
result_csv = parser2.invoke(response)

print("문자열결과: ", result_str)
print("CSV결과: ", result_csv)

# 1.입력정의(Prompt) => 2.LLM => 3.결과파싱

"""
물론입니다! 다음은 테슬라 Model S를 홍보하기 위한 캐치프레이즈 5개입니다:

"전기차의 미래, 테슬라 Model S", "속도와 지속 가능성을 만나다, Model S", "한 번의 충전으로 끝없는 여정, 테슬라 Model S", "혁신의 아이콘, Model S와 함께하세요", "모두를 위한 럭셔리 전기차, 테슬라 Model S" 

이 내용은 다음과 같이 CSV 형식으로 제공합니다:
```
전기차의 미래, 테슬라 Model S, 속도와 지속 가능성을 만나다, Model S, 한 번의 충전으로 끝없는 여정, 테슬라 Model S, 혁신의 아이콘, Model S와 함께하세요, 모두를 위한 럭셔리 전기차, 테슬라 Model S
```
문자열결과:  물론입니다! 다음은 테슬라 Model S를 홍보하기 위한 캐치프레이즈 5개입니다:

"전기차의 미래, 테슬라 Model S", "속도와 지속 가능성을 만나다, Model S", "한 번의 충전으로 끝없는 여정, 테슬라 Model S", "혁신의 아이콘, Model S와 함께하세요", "모두를 위한 럭셔리 전기차, 테슬라 Model S" 

이 내용은 다음과 같이 CSV 형식으로 제공합니다:
```
전기차의 미래, 테슬라 Model S, 속도와 지속 가능성을 만나다, Model S, 한 번의 충전으로 끝없는 여정, 테슬라 Model S, 혁신의 아이콘, Model S와 함께하세요, 모두를 위한 럭셔리 전기차, 테슬라 Model S
```
CSV결과:  ['물론입니다! 다음은 테슬라 Model S를 홍보하기 위한 캐치프레이즈 5개입니다:', '전기차의 미래, 테슬라 Model S', '속도와 지속 가능성을 만나다, Model S', '한 번의 충전으로 끝없는 여정, 테슬라 Model S', '혁신의 아이콘, Model S와 함께하세요', '모두를 위한 럭셔리 전기차, 테슬라 Model S ', '이 내용은 다음과 같이 CSV 형식으로 제공합니다:', '```', '전기차의 미래', '테슬라 Model S', '속도와 지속 가능성을 만나다', 'Model S', '한 번의 충전으로 끝없는 여정', '테슬라 Model S', '혁신의 아이콘', 'Model S와 함께하세요', '모두를 위한 럭셔리 전기차', '테슬라 Model S', '```']
"""