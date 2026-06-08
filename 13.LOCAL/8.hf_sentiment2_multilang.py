from transformers import pipeline

# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

# Classify a new sentence
# sentence = "I love this product! It's amazing and works perfectly."
# result = pipe(sentence)

# Print the result
# print(result)

"""
Loading weights: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 104/104 [00:00<00:00, 7349.63it/s]
[{'label': 'Very Positive', 'score': 0.558630645275116}]
"""

comments = [
    "정말 만족스러운 제품입니다. 다음에도 다시 구매할 것 같아요.",
    "생각보다 품질이 좋아서 놀랐습니다.",
    "배송이 너무 늦어서 불편했습니다.",
    "가격은 비싸지만 성능은 확실히 좋네요.",
    "기대한 것보다 별로였고 다시 구매하고 싶지 않습니다.",
    "그냥 무난한 제품인 것 같습니다.",
    "사용하기 편하고 기능도 다양해서 만족합니다.",
    "고객센터 응대가 불친절해서 아쉬웠습니다.",
    "디자인은 예쁘지만 내구성이 조금 약한 것 같아요.",
    "전반적으로 만족스럽고 주변 사람들에게 추천하고 싶습니다."
]

for comment in comments:
    result = pipe(comment)
    print(f"문장: {comment}")
    print(f"결과: {result}\n")

"""
문장: 정말 만족스러운 제품입니다. 다음에도 다시 구매할 것 같아요.
결과: [{'label': 'Positive', 'score': 0.8869256973266602}]

문장: 생각보다 품질이 좋아서 놀랐습니다.
결과: [{'label': 'Positive', 'score': 0.8158912062644958}]

문장: 배송이 너무 늦어서 불편했습니다.
결과: [{'label': 'Negative', 'score': 0.8574267625808716}]

문장: 가격은 비싸지만 성능은 확실히 좋네요.
결과: [{'label': 'Positive', 'score': 0.7918226718902588}]

문장: 기대한 것보다 별로였고 다시 구매하고 싶지 않습니다.
결과: [{'label': 'Negative', 'score': 0.7601073384284973}]

문장: 그냥 무난한 제품인 것 같습니다.
결과: [{'label': 'Neutral', 'score': 0.8799977898597717}]

문장: 사용하기 편하고 기능도 다양해서 만족합니다.
결과: [{'label': 'Positive', 'score': 0.9208890795707703}]

문장: 고객센터 응대가 불친절해서 아쉬웠습니다.
결과: [{'label': 'Negative', 'score': 0.8825998902320862}]

문장: 디자인은 예쁘지만 내구성이 조금 약한 것 같아요.
결과: [{'label': 'Negative', 'score': 0.9313780069351196}]

문장: 전반적으로 만족스럽고 주변 사람들에게 추천하고 싶습니다.
결과: [{'label': 'Positive', 'score': 0.8937059044837952}]
"""

