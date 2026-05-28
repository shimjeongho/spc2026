from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

def make_chain(role):
    return (
        ChatPromptTemplate.from_messages([
            ("system", role),
            ("user", "{question}")
        ])
        | llm
        | StrOutputParser()
    )

# 개발자냐/요리사냐/일반
code_chain = make_chain("당신은 파이썬 개발자입니다.")
cook_chain = make_chain("당신은 요리 전문가입니다.")
general_chain = make_chain("당신은 일반 어시스턴트 입니다.")

branch = RunnableBranch(
    (
        lambda x: "파이썬" in x["question"] or "코드" in x["question"],
        code_chain
    ),
    (
        lambda x: "요리" in x["question"] or "레시피" in x["question"],
        cook_chain
    ),
    general_chain
)

questions = [
    "파이썬 리스트 정렬 코드 알려줘",
    "김치찌개 레시피 알려줘",
    "오늘 날씨 어때?"
]

for q in questions:
    print("질문:", q)
    print("답변:", branch.invoke({"question": q}))
    print('-' * 60)

"""
질문: 파이썬 리스트 정렬 코드 알려줘
답변: 파이썬에서 리스트를 정렬하는 방법은 여러 가지가 있습니다. 가장 흔히 사용되는 두 가지 방법은 `sort()` 메서드와 `sorted()` 함수를 사용하는 것입니다. 아래에서 각각의 방법을 설명하겠습니다.

### 1. `sort()` 메서드

`sort()` 메서드는 리스트 객체에 대해 직접 호출되어 리스트를 정렬합니다. 이 메서드는 원본 리스트를 변경합니다.

```python
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()  # 리스트를 오름차순으로 정렬
print(my_list)  # 출력: [1, 2, 5, 5, 6, 9]
```

내림차순으로 정렬하려면 `reverse` 매개변수를 사용할 수 있습니다.

```python
my_list.sort(reverse=True)  # 리스트를 내림차순으로 정렬
print(my_list)  # 출력: [9, 6, 5, 5, 2, 1]
```

### 2. `sorted()` 함수

`sorted()` 함수는 리스트를 정렬한 새 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.

```python
my_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(my_list)  # 리스트를 오름차순으로 정렬한 새 리스트 생성
print(sorted_list)  # 출력: [1, 2, 5, 5, 6, 9]
print(my_list)      # 원본 리스트는 그대로: [5, 2, 9, 1, 5, 6]
```

내림차순으로 정렬하려면 `reverse` 매개변수를 사용할 수 있습니다.

```python
sorted_list_desc = sorted(my_list, reverse=True)  # 리스트를 내림차순으로 정렬한 새 리스트 생성
print(sorted_list_desc)  # 출력: [9, 6, 5, 5, 2, 1]
```

### 사용자 정의 정렬

리스트의 요소를 사용자 정의 기준에 따라 정렬하려면 `key` 매개변수를 사용할 수 있습니다. 예를 들어, 문자열 리스트를 길이에 따라 정렬할 수 있습니다.

```python
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)  # 문자열의 길이에 따라 정렬
print(words)  # 출력: ['pie', 'book', 'banana', 'Washington']
```

이렇게 파이썬에서 리스트를 정렬하는 방법을 확인해 보았습니다. 필요에 따라 적절한 방법을 선택하여 사용하시면 됩니다!
------------------------------------------------------------
질문: 김치찌개 레시피 알려줘
답변: 김치찌개는 한국의 대표적인 찌개 중 하나로, 매콤하고 깊은 맛이 특징입니다. 여기에서 기본적인 김치찌개 레시피를 소개할게요.

### 재료
- 김치 2컵 (숙성된 김치가 가장 맛있습니다)
- 돼지고기 (목살 또는 삼겹살) 200g
- 두부 1/2모
- 양파 1개
- 대파 1대
- 마늘 3~4쪽 (다진 것)
- 고춧가루 1~2큰술 (취향에 맞게 조절)
- 국간장 1~2큰술
- 소금, 후추 약간
- 물 4컵
- 식용유 1큰술 (선택 사항)

### 조리 과정
1. **재료 손질하기**:
   - 김치는 먹기 좋은 크기로 자르고, 돼지고기는 한 입 크기로 썰어줍니다.
   - 두부는 깍둑썰기로 자르고, 양파는 채 썰고, 대파는 어슷썰기 합니다.

2. **고기 볶기**:
   - 중간 불에 냄비에 식용유를 두르고, 돼지고기를 넣고 볶아줍니다. 고기 색이 변할 때까지 볶아주세요.

3. **김치 추가하기**:
   - 돼지고기가 볶아지면, 준비한 김치를 넣고 함께 볶아줍니다. 김치가 약간 투명해질 때까지 볶습니다.

4. **국물 만들기**:
   - 물 4컵을 붓고 끓입니다. 끓기 시작하면, 마늘, 고춧가루, 국간장을 넣고 잘 섞어주세요.

5. **재료 넣기**:
   - 국물이 끓어오르면 양파와 두부를 넣고, 소금과 후추로 간을 맞춥니다.

6. **마무리**:
   - 찌개가 끓으면 대파를 넣고 5~10분 정도 중약 불에서 더 끓입니다. 김치와 돼지고기가 잘 익으면 완성입니다.

7. **서빙**:
   - 완성된 김치찌개를 그릇에 담아 밥과 함께 따뜻하게 즐기세요. 추가로 고추나 다진 쪽파를 위에 올려주면 더욱 맛있습니다.

맛있게 드세요! 김치찌개는 개인의 취향에 따라 재료와 양념을 조절하면 더욱 다양하게 즐길 수 있습니다.
------------------------------------------------------------
질문: 오늘 날씨 어때?
답변: 죄송하지만, 실시간 날씨 정보를 제공할 수 없습니다. 현재 위치의 날씨를 확인하려면 기상 웹사이트나 날씨 앱을 사용해 보세요. 도움이 필요하시면 언제든지 말씀해 주세요!
------------------------------------------------------------
"""