# 나만의 데이터로 모델 추가 학습하기 (fine-tuning)
# pip install transformers torch datasets

import numpy as np
from transformers import (
    AutoModelForSequenceClassification,  # 텍스트 분류 모델 자동 로드
    AutoTokenizer,                       # 토크나이저 자동 로드
    Trainer,                             # 학습을 쉽게 해주는 클래스
    TrainingArguments                    # 학습 설정 클래스
)
from datasets import Dataset

# 학습 데이터 추가 (1=긍정, 0=부정)
train_data = {
    "text": [
        "정말 마음에 들어요.",
        "최악의 경험이었어요.",
        "오늘 기분이 너무 좋아요.",
        "너무 실망스러웠어요.",
        "이 제품은 정말 훌륭합니다.",
        "다시는 이용하고 싶지 않아요.",
        "서비스가 매우 만족스러웠습니다.",
        "시간과 돈이 아까웠어요.",
        "배송이 빨라서 좋았어요.",
        "품질이 기대 이하였어요."
    ],
    "label": [
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0
    ]
}

eval_data = {
    "text": [
        "오늘 하루가 행복했어요.",
        "직원 태도가 너무 불친절했어요.",
        "기대한 것보다 훨씬 좋네요.",
        "정말 별로였어요."
    ],
    "label": [
        1, 0, 1, 0
    ]
}

# 사전학습된 DistilBERT 모델 사용

# BERT보다 가벼움
# 속도 빠름
# 텍스트 분류에 자주 사용
model_name = "beomi/kcbert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# padding : 길이가 짧은 문장은 뒤에 0 추가, truncation: 문장이 너무 길면 잘라냄
def tokenize(batch):
    return tokenizer(batch['text'], padding="max_length", truncation=True)

# Dataset 생성
train_ds = Dataset.from_dict(train_data).map(tokenize, batched=True)
# 평가 데이터도 데이터 셋
eval_ds = Dataset.from_dict(eval_data).map(tokenize, batched=True)

# 모델 로드
# 텍스트 분류 모델 생성
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=2,
    # 숫자 → 문자
    id2label={0: "부정", 1: "긍정"},
    # 문자 → 숫자
    label2id={"부정": 0, "긍정": 1}
)

# 정확도 계산 함수
def compute_metrics(eval_pred):
    # 예측값과 정답 분리
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)  # 가장 큰 값을 선택
    return {"accuracy": float((preds == labels).mean())}

# 학습 설정
args = TrainingArguments(
    output_dir="./results_kr", # 학습 결과 저장 폴더
    eval_strategy="epoch", # 1 epoch마다 평가
    save_strategy="epoch", # 1 epoch마다 모델 저장
    per_device_train_batch_size=2, # 한 번에 2개 데이터 학습
    per_device_eval_batch_size=2, # 평가도 2개씩
    num_train_epochs=20, # 전체 데이터를 5번 반복 학습   
    logging_steps=1 # 매 step마다 로그 출력
)

# Trainer 생성
trainer = Trainer(
    model=model, args=args,
    train_dataset=train_ds, eval_dataset=eval_ds,
    compute_metrics=compute_metrics
)

trainer.train()
print("평가 결과:", trainer.evaluate())

save_path="./my_local_model_kr"
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
print("내 모델 저장 완료: ", save_path)

"""
[transformers] BertForSequenceClassification LOAD REPORT from: beomi/kcbert-base
Key                                        | Status     | Details
-------------------------------------------+------------+--------
cls.seq_relationship.weight                | UNEXPECTED |        
cls.predictions.transform.dense.bias       | UNEXPECTED |        
cls.predictions.transform.dense.weight     | UNEXPECTED |        
cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |        
cls.predictions.transform.LayerNorm.weight | UNEXPECTED |        
cls.seq_relationship.bias                  | UNEXPECTED |        
cls.predictions.bias                       | UNEXPECTED |        
classifier.bias                            | MISSING    |        
classifier.weight                          | MISSING    |        

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
  0%|                                                                                                                                                                             | 0/25 [00:00<?, ?it/s]C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.4845', 'grad_norm': '13.26', 'learning_rate': '5e-05', 'epoch': '0.2'}                                                                                                                       
{'loss': '0.9987', 'grad_norm': '18.28', 'learning_rate': '4.8e-05', 'epoch': '0.4'}                                                                                                                     
{'loss': '1.262', 'grad_norm': '20.29', 'learning_rate': '4.6e-05', 'epoch': '0.6'}                                                                                                                      
{'loss': '0.7447', 'grad_norm': '15.75', 'learning_rate': '4.4e-05', 'epoch': '0.8'}                                                                                                                     
{'loss': '0.8405', 'grad_norm': '23.14', 'learning_rate': '4.2e-05', 'epoch': '1'}                                                                                                                       
{'eval_loss': '0.7777', 'eval_accuracy': '0.5', 'eval_runtime': '1.178', 'eval_samples_per_second': '3.397', 'eval_steps_per_second': '1.698', 'epoch': '1'}                                             
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.83s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.7993', 'grad_norm': '25.46', 'learning_rate': '4e-05', 'epoch': '1.2'}                                                                                                                       
{'loss': '0.6704', 'grad_norm': '18.26', 'learning_rate': '3.8e-05', 'epoch': '1.4'}                                                                                                                     
{'loss': '0.1709', 'grad_norm': '5.761', 'learning_rate': '3.6e-05', 'epoch': '1.6'}                                                                                                                     
{'loss': '0.5476', 'grad_norm': '18.94', 'learning_rate': '3.4e-05', 'epoch': '1.8'}                                                                                                                     
{'loss': '0.4178', 'grad_norm': '13.99', 'learning_rate': '3.2e-05', 'epoch': '2'}                                                                                                                       
{'eval_loss': '0.7181', 'eval_accuracy': '0.5', 'eval_runtime': '1.804', 'eval_samples_per_second': '2.218', 'eval_steps_per_second': '1.109', 'epoch': '2'}                                             
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.71s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.516', 'grad_norm': '20.55', 'learning_rate': '3e-05', 'epoch': '2.2'}                                                                                                                        
{'loss': '0.6419', 'grad_norm': '13.82', 'learning_rate': '2.8e-05', 'epoch': '2.4'}                                                                                                                     
{'loss': '0.2622', 'grad_norm': '9.747', 'learning_rate': '2.6e-05', 'epoch': '2.6'}                                                                                                                     
{'loss': '0.1318', 'grad_norm': '3.673', 'learning_rate': '2.4e-05', 'epoch': '2.8'}                                                                                                                     
{'loss': '0.1779', 'grad_norm': '5.033', 'learning_rate': '2.2e-05', 'epoch': '3'}                                                                                                                       
{'eval_loss': '0.5697', 'eval_accuracy': '0.75', 'eval_runtime': '1.297', 'eval_samples_per_second': '3.083', 'eval_steps_per_second': '1.542', 'epoch': '3'}                                            
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.28s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.2429', 'grad_norm': '6.877', 'learning_rate': '2e-05', 'epoch': '3.2'}                                                                                                                       
{'loss': '0.1116', 'grad_norm': '4.728', 'learning_rate': '1.8e-05', 'epoch': '3.4'}                                                                                                                     
{'loss': '0.1948', 'grad_norm': '6.291', 'learning_rate': '1.6e-05', 'epoch': '3.6'}                                                                                                                     
{'loss': '0.218', 'grad_norm': '8.999', 'learning_rate': '1.4e-05', 'epoch': '3.8'}                                                                                                                      
{'loss': '0.06489', 'grad_norm': '2.012', 'learning_rate': '1.2e-05', 'epoch': '4'}                                                                                                                      
{'eval_loss': '0.4961', 'eval_accuracy': '0.75', 'eval_runtime': '1.072', 'eval_samples_per_second': '3.731', 'eval_steps_per_second': '1.866', 'epoch': '4'}                                            
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.19s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.05195', 'grad_norm': '1.758', 'learning_rate': '1e-05', 'epoch': '4.2'}                                                                                                                      
{'loss': '0.03092', 'grad_norm': '1.035', 'learning_rate': '8e-06', 'epoch': '4.4'}                                                                                                                      
{'loss': '0.1151', 'grad_norm': '4.547', 'learning_rate': '6e-06', 'epoch': '4.6'}                                                                                                                       
{'loss': '0.09263', 'grad_norm': '3.687', 'learning_rate': '4e-06', 'epoch': '4.8'}                                                                                                                      
{'loss': '0.04994', 'grad_norm': '1.589', 'learning_rate': '2e-06', 'epoch': '5'}                                                                                                                        
{'eval_loss': '0.4528', 'eval_accuracy': '0.75', 'eval_runtime': '1.163', 'eval_samples_per_second': '3.44', 'eval_steps_per_second': '1.72', 'epoch': '5'}                                              
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.06s/it]
{'train_runtime': '110.4', 'train_samples_per_second': '0.453', 'train_steps_per_second': '0.226', 'train_loss': '0.3936', 'epoch': '5'}                                                                 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 25/25 [01:50<00:00,  4.42s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  3.63it/s]
평가 결과: {'eval_loss': 0.45279502868652344, 'eval_accuracy': 0.75, 'eval_runtime': 1.0987, 'eval_samples_per_second': 3.641, 'eval_steps_per_second': 1.82, 'epoch': 5.0}
Writing model shards: 100%|█████████████████
"""