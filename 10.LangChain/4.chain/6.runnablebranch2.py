from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

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
code_chain = (
    RunnableLambda(lambda x: print(">>> 개발자 코드 실행") or x)
    | make_chain("당신은 파이썬 개발자입니다.")
) 
cook_chain = (
    RunnableLambda(lambda x: print(">>> 요리사 코드 실행") or x)
    | make_chain("당신은 요리 전문가입니다.")
) 
general_chain = (
    RunnableLambda(lambda x: print(">>> 일반 코드 실행") or x)
    | make_chain("당신은 일반 어시스턴트 입니다.")
) 

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
    "오늘 날씨 어때?",
    "된장찌개 파이썬 레시피 알려줘"
]

for q in questions:
    print("질문:", q)
    print("답변:", branch.invoke({"question": q}))
    print('-' * 60)

"""
질문: 파이썬 리스트 정렬 코드 알려줘
>>> 개발자 코드 실행
답변: 파이썬에서 리스트를 정렬하는 방법은 여러 가지가 있습니다. 가장 기본적인 방법은 `sort()` 메서드를 사용하거나 `sorted()` 함수를 사용하는 것입니다.

1. **`sort()` 메서드**: 이 메서드는 리스트 자체를 정렬합니다. 원본 리스트가 변경됩니다.

```python
# 정렬할 리스트
numbers = [5, 2, 9, 1, 5, 6]

# 리스트 정렬
numbers.sort()

# 정렬된 리스트 출력
print(numbers)  # 결과: [1, 2, 5, 5, 6, 9]
```

2. **`sorted()` 함수**: 이 함수는 정렬된 새로운 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.

```python
# 정렬할 리스트
numbers = [5, 2, 9, 1, 5, 6]

# 리스트 정렬
sorted_numbers = sorted(numbers)

# 정렬된 리스트 출력
print(sorted_numbers)  # 결과: [1, 2, 5, 5, 6, 9]

# 원본 리스트는 변경되지 않음
print(numbers)  # 결과: [5, 2, 9, 1, 5, 6]
```

3. **내림차순 정렬**: `sort()`와 `sorted()` 모두 `reverse=True` 인자를 사용하여 내림차순으로 정렬할 수 있습니다.

```python
# 내림차순 정렬 using sort()
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)
print(numbers)  # 결과: [9, 6, 5, 5, 2, 1]

# 내림차순 정렬 using sorted()
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # 결과: [9, 6, 5, 5, 2, 1]
```

리스트가 문자열을 포함하고 있는 경우에 대해서도 동일한 방법으로 정렬할 수 있습니다. 예를 들어:

```python
# 문자열 리스트 정렬
words = ["banana", "apple", "cherry"]
words.sort()
print(words)  # 결과: ['apple', 'banana', 'cherry']
```

이렇게 파이썬에서 리스트를 정렬할 수 있습니다! 추가적인 질문이 있다면 언제든지 물어보세요.
------------------------------------------------------------
질문: 김치찌개 레시피 알려줘
>>> 요리사 코드 실행
답변: 김치찌개는 한국의 전통 찌개로, 매콤하고 깊은 맛이 특징입니다. 아래는 기본적인 김치찌개 레시피입니다.

### 재료
- 잘 익은 김치 2컵
- 돼지고기 (삼겹살 또는 목살) 200g
- 두부 1/2모
- 양파 1개
- 대파 1대
- 마늘 2~3쪽
- 고추가루 1~2큰술
- 국물용 다시마 (옵션)
- 물 4컵
- 소금, 후추, 간장 (간은 취향에 따라)

### 만들기
1. **재료 손질하기**
   - 김치는 한 입 크기로 썰고, 돼지고기는 먹기 좋은 크기로 자릅니다.
   - 양파는 채썰고, 대파는 어슷하게 썰고, 마늘은 다져놓습니다.
   - 두부는 깍둑썰기합니다.

2. **고기 볶기**
   - 냄비에 돼지고기를 넣고 중불에서 볶아줍니다. 고기가 어느 정도 익으면 마늘과 양파를 넣고 함께 볶습니다.

3. **김치 추가하기**
   - 볶은 고기와 양파 위에 김치를 넣고 3~5분 동안 볶아줍니다. 김치가 조금 익으면 고추가루를 넣고 잘 섞습니다.

4. **국물 넣기**
   - 물을 넣고 끓여줍니다. 필요시 다시마를 넣어 국물을 우려내면 더욱 깊은 맛을 얻을 수 있습니다.

5. **조리하기**
   - 끓어오르면 중불로 줄이고 15~20분 정도 끓입니다. 이때 두부를 넣고 소금과 후추로 간을 맞추고, 원하는 경우 간장을 조금 추가할 수 있습니다.

6. **마무리**
   - 대파를 넣고 5분 정도 더 끓인 후 불을 끕니다.
   - 기호에 따라 추가 매운 고추를 넣기도 합니다.

### 서빙
- 완성된 김치찌개는 밥과 함께 따뜻하게 서빙하고, 김치와 함께 즐기면 더욱 맛있습니다.

맛있게 만들어 드세요!
------------------------------------------------------------
질문: 오늘 날씨 어때?
>>> 일반 코드 실행
답변: 죄송하지만, 실시간 날씨 정보는 제공할 수 없습니다. 현재 위치의 날씨를 확인하려면 기상청 웹사이트나 날씨 앱을 이용해 보세요. 다른 질문이 있으시면 도와드리겠습니다!
------------------------------------------------------------
질문: 된장찌개 파이썬 레시피 알려줘
>>> 개발자 코드 실행
답변: 된장찌개를 만드는 파이썬 레시피 코드를 작성해보겠습니다. 이 코드는 재료를 정의하고, 준비 및 요리 과정을 함수로 나누어 표현합니다.

```python
class DoenjangJjigae:
    def __init__(self):
        self.ingredients = {
            '된장': '2 큰술',
            '물': '4컵',
            '두부': '1/2모',
            '애호박': '1/2개',
            '버섯': '100g',
            '양파': '1개',
            '대파': '1대',
            '고추': '1개',
            '마늘': '2쪽',
            '소금': '적당량',
            '후춧가루': '적당량'
        }

    def prepare_ingredients(self):
        print("재료를 준비합니다:")
        for ingredient, amount in self.ingredients.items():
            print(f"{ingredient}: {amount}")

    def cook(self):
        print("\n된장찌개를 요리합니다:")
        print("1. 물을 끓입니다.")
        print("2. 된장을 풀어 넣습니다.")
        print("3. 애호박, 양파, 버섯, 두부를 넣고 끓입니다.")
        print("4. 마늘, 대파, 고추를 넣습니다.")
        print("5. 간을 보면서 소금과 후춧가루로 간을 맞춥니다.")
        print("6. 모든 재료가 잘 익으면 불을 끕니다.")
        print("된장찌개가 완성되었습니다!")

if __name__ == "__main__":
    jjigae = DoenjangJjigae()
    jjigae.prepare_ingredients()
    jjigae.cook()
```

이 코드를 실행하면, 된장찌개를 만들기 위한 재료 리스트와 요리 과정을 출력합니다. 각 단계는 요리가 진행되는 과정을 직관적으로 보여 줍니다. 필요한 경우 재료나 양을 조절하여 원하는 맛을 낼 수 있습니다.
------------------------------------------------------------
"""