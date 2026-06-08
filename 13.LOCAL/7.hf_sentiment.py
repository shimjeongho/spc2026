# 분류 (text clssification)
# pip install transformers torch
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
# {아키텍처}-{크기}-{전처리방식}-{학습방식}-{데이터셋}-{언어}

result = sentiment_analyzer("I'm hungry")
print(result)

result = sentiment_analyzer("I'm tired")
print(result)

result = sentiment_analyzer("I'm happy")
print(result)
print(result[0]['label'])

"""
Loading weights: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 104/104 [00:00<00:00, 6366.32it/s]
[{'label': 'NEGATIVE', 'score': 0.9988470077514648}]
[{'label': 'NEGATIVE', 'score': 0.999774158000946}]
[{'label': 'POSITIVE', 'score': 0.9998793601989746}]
POSITIVE
"""