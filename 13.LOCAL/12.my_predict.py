import os
from transformers import pipeline

MODEL_DIR = "./my_local_model"

classifier = pipeline("sentiment-analysis", model=MODEL_DIR, tokenizer=MODEL_DIR)

test_sentences = [
    "I love using my own AI model!",
    "This is the worst experience ever.",
    "This is the best experience ever.",
    "I feel so bad..."
]

for text in test_sentences:
    r = classifier(text)[0]
    print(f"문장: {text}, 결과 {r['label']}, 점수: {r['score']:.3f}")

"""
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 104/104 [00:00<00:00, 15915.34it/s]
문장: I love using my own AI model!, 결과 POSITIVE, 점수: 0.522
문장: This is the worst experience ever., 결과 NEGATIVE, 점수: 0.744
문장: This is the best experience ever., 결과 NEGATIVE, 점수: 0.677
문장: I feel so bad..., 결과 NEGATIVE, 점수: 0.645
"""