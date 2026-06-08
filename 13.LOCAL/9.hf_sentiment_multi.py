from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

text = "이 영화 정말 재미있었어요?"

inputs = tokenizer(text, return_tensors="pt", trucation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()

# 이 모델의 결과값은 5가지 class (0~4)
print(f"예측된 감정 점수: {predicted_class}")

"""
vocab.txt: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 872k/872k [00:00<00:00, 43.1MB/s]
special_tokens_map.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 112/112 [00:00<?, ?B/s]
config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 953/953 [00:00<?, ?B/s]
model.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 669M/669M [00:16<00:00, 41.4MB/s]
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 201/201 [00:00<00:00, 11737.30it/s]
예측된 감정 점수: 2
"""

texts = ["이 식장 너무 별로였어요", "여기 서비스 정말 최고에요!", "그냥 먹을만하네요"]
inputs = tokenizer(text, return_tensors="pt", trucation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()
    predictions = torch.argmax(logits, dim=1)

for text, pred in zip(texts, predictions):
    print(f"문장 {text} -> 감정 점수 {pred.item() + 1}")

"""
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 201/201 [00:00<00:00, 84246.54it/s]
예측된 감정 점수: 2
문장 이 식장 너무 별로였어요 -> 감정 점수 3

"""