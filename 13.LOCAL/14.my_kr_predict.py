import os
from transformers import pipeline

MODEL_DIR = "./my_local_model"

classifier = pipeline("sentiment-analysis", model=MODEL_DIR, tokenizer=MODEL_DIR)

test_sentences = [
    "정말 마음에 들어요.",
    "오늘 하루가 너무 행복합니다.",
    "서비스가 친절해서 만족스러웠어요.",
    "배송이 빨라서 좋았습니다.",
    "이 제품은 기대 이상이에요.",

    "최악의 경험이었어요.",
    "정말 실망했습니다.",
    "다시는 이용하고 싶지 않아요.",
    "시간과 돈이 아까웠어요.",
    "품질이 너무 별로네요."
]

for text in test_sentences:
    r = classifier(text)[0]
    print(f"문장: {text}, 결과 {r['label']}, 점수: {r['score']:.3f}")

"""
Loading weights: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 104/104 [00:00<00:00, 3431.06it/s]
문장: 정말 마음에 들어요., 결과 POSITIVE, 점수: 0.555
문장: 오늘 하루가 너무 행복합니다., 결과 POSITIVE, 점수: 0.557
문장: 서비스가 친절해서 만족스러웠어요., 결과 POSITIVE, 점수: 0.566
문장: 배송이 빨라서 좋았습니다., 결과 POSITIVE, 점수: 0.551
문장: 이 제품은 기대 이상이에요., 결과 POSITIVE, 점수: 0.567
문장: 최악의 경험이었어요., 결과 NEGATIVE, 점수: 0.515
문장: 정말 실망했습니다., 결과 POSITIVE, 점수: 0.538
문장: 다시는 이용하고 싶지 않아요., 결과 POSITIVE, 점수: 0.558
문장: 시간과 돈이 아까웠어요., 결과 POSITIVE, 점수: 0.565
문장: 품질이 너무 별로네요., 결과 POSITIVE, 점수: 0.561
"""