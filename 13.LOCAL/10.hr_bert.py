from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# MNLI = Multi-Genre Natural Language Inference
# 내부적으로는... 문장/문장 연관성
# 1. 함의(Entailment)
# 예) 오늘 비가 많이 내린다.
#     우산이 필요할 수 있다.
# 2. 모순(Contradiction)
# 예) 오늘 비가 많이 내린다.
#     오늘은 맑은 날이다.
# 3. 중립 (Natural)
# 예) 오늘 비가 많이 내린다.
#     나는 피자를 좋아한다.

text = "I just upgraded my computer's graphics card"
texts = [
    # technology
    "I just upgraded my computer's graphics card.",

    # sports
    "Our team won the soccer championship after an intense final match.",

    # cooking
    "I spent the weekend making homemade pasta and baking a cake.",

    # politics
    "The parliament passed a new tax reform bill yesterday.",

    # technology + politics
    "The government announced a major investment in artificial intelligence research.",

    # technology + sports
    "The football team uses AI software to analyze player performance.",

    # technology + cooking
    "My smart oven automatically adjusts the temperature while cooking dinner.",

    # politics + sports
    "The president attended the national football championship game.",

    # technology + politics + cooking
    "A government-funded AI nutrition platform was launched this week.",

    # technology + sports + cooking
    "The athletes use advanced data analytics to optimize their training and diet plans."
]
# 나는 내 컴퓨터의 그래픽 카드를 업그레이드 했다.
# 이 문장은 기술에 관한 것이다.
# 이 문장은 스포츠에 관한 것이다.
# 이 문장은 요리에 관한 것이다.
# 이 문장은 정치에 관한 것이다.

candidate_labels = ["technology", "sports", "cooking", "politics"]


for text in texts:
    result = classifier(text, candidate_labels=candidate_labels)



    print(f"문장: {text}")
    for label, score in zip(result["labels"], result["scores"]):
        print(f"{label:12} {score:.3f}")

    print(f"최종 분류: {result['labels'][0]}")


"""
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 515/515 [00:00<00:00, 23753.70it/s]
문장: I just upgraded my computer's graphics card.
technology   0.970
sports       0.019
politics     0.006
cooking      0.005
최종 분류: technology
문장: Our team won the soccer championship after an intense final match.
sports       0.996
technology   0.002
cooking      0.001
politics     0.001
최종 분류: sports
문장: I spent the weekend making homemade pasta and baking a cake.
cooking      0.989
technology   0.007
sports       0.003
politics     0.002
최종 분류: cooking
문장: The parliament passed a new tax reform bill yesterday.
politics     0.720
technology   0.139
cooking      0.092
sports       0.049
최종 분류: politics
문장: The government announced a major investment in artificial intelligence research.
technology   0.971
politics     0.015
sports       0.007
cooking      0.007
최종 분류: technology
문장: The football team uses AI software to analyze player performance.
sports       0.722
technology   0.276
cooking      0.001
politics     0.001
최종 분류: sports
문장: My smart oven automatically adjusts the temperature while cooking dinner.
cooking      0.511
technology   0.486
sports       0.002
politics     0.001
최종 분류: cooking
문장: The president attended the national football championship game.
sports       0.989
politics     0.007
technology   0.003
cooking      0.002
최종 분류: sports
문장: A government-funded AI nutrition platform was launched this week.
technology   0.968
cooking      0.026
sports       0.004
politics     0.003
최종 분류: technology
문장: The athletes use advanced data analytics to optimize their training and diet plans.
sports       0.588
technology   0.406
cooking      0.004
politics     0.003
최종 분류: sports
"""