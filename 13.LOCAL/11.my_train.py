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
    "text": ["I love this!", "This is terrible!", "I an happy", "I am sad", "This product is amazing", "Worst experience ever.", "Absolutly fantastic", "I hate it."],
    "label": [1, 0, 1, 0, 1, 0, 1, 0]
}
# 평가용 데이터
eval_data = {
    "text": ["I fell greate today!", "The service was awful", "I'm super excited about this!", "Not what I expected"],
    "label": [1, 0, 1, 0]
}

# 사전학습된 DistilBERT 모델 사용

# BERT보다 가벼움
# 속도 빠름
# 텍스트 분류에 자주 사용
model_name = "distilbert-base-uncased"

# 문장을 모델이 이해할 수 있는 숫자로 변환하는 도구
# 예시

# "I love this!"

# ↓

# [101, 1045, 2293, 2023, 999, 102]
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
    id2label={0: "NEGATIVE", 1: "POSITIVE"},
    # 문자 → 숫자
    label2id={"NEGATIVE": 0, "POSITIVE": 1}
)

# 정확도 계산 함수
def compute_metrics(eval_pred):
    # 예측값과 정답 분리
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)  # 가장 큰 값을 선택
    return {"accuracy": float((preds == labels).mean())}

# 학습 설정
args = TrainingArguments(
    output_dir="./results", # 학습 결과 저장 폴더
    eval_strategy="epoch", # 1 epoch마다 평가
    save_strategy="epoch", # 1 epoch마다 모델 저장
    per_device_train_batch_size=2, # 한 번에 2개 데이터 학습
    per_device_eval_batch_size=2, # 평가도 2개씩
    num_train_epochs=5, # 전체 데이터를 5번 반복 학습   
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

save_path="./my_local_model"
trainer.save_model(save_path)
tokenizer.save_pretrained(save_path)
print("내 모델 저장 완료: ", save_path)

"""
Map: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 1627.35 examples/s]
Map: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 391.94 examples/s]
Loading weights: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 6444.15it/s]
[transformers] DistilBertForSequenceClassification LOAD REPORT from: distilbert-base-uncased
Key                     | Status     | Details
------------------------+------------+--------
vocab_projector.bias    | UNEXPECTED |        
vocab_transform.weight  | UNEXPECTED |        
vocab_layer_norm.bias   | UNEXPECTED |        
vocab_layer_norm.weight | UNEXPECTED |        
vocab_transform.bias    | UNEXPECTED |        
classifier.bias         | MISSING    |        
classifier.weight       | MISSING    |        
pre_classifier.weight   | MISSING    |        
pre_classifier.bias     | MISSING    |        

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
  0%|                                                                                                                                                                             | 0/20 [00:00<?, ?it/s]C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.692', 'grad_norm': '2.176', 'learning_rate': '5e-05', 'epoch': '0.25'}                                                                                                                       
{'loss': '0.7103', 'grad_norm': '2.533', 'learning_rate': '4.75e-05', 'epoch': '0.5'}                                                                                                                    
{'loss': '0.7025', 'grad_norm': '2.934', 'learning_rate': '4.5e-05', 'epoch': '0.75'}                                                                                                                    
{'loss': '0.6896', 'grad_norm': '3.294', 'learning_rate': '4.25e-05', 'epoch': '1'}                                                                                                                      
{'eval_loss': '0.7038', 'eval_accuracy': '0.25', 'eval_runtime': '0.9469', 'eval_samples_per_second': '4.224', 'eval_steps_per_second': '2.112', 'epoch': '1'}                                           
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.12it/s]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.6462', 'grad_norm': '3.25', 'learning_rate': '4e-05', 'epoch': '1.25'}                                                                                                                       
{'loss': '0.6323', 'grad_norm': '6.764', 'learning_rate': '3.75e-05', 'epoch': '1.5'}                                                                                                                    
{'loss': '0.642', 'grad_norm': '3.782', 'learning_rate': '3.5e-05', 'epoch': '1.75'}                                                                                                                     
{'loss': '0.6881', 'grad_norm': '6.554', 'learning_rate': '3.25e-05', 'epoch': '2'}                                                                                                                      
{'eval_loss': '0.7411', 'eval_accuracy': '0.25', 'eval_runtime': '0.9288', 'eval_samples_per_second': '4.306', 'eval_steps_per_second': '2.153', 'epoch': '2'}                                           
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.02it/s]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.5129', 'grad_norm': '3.668', 'learning_rate': '3e-05', 'epoch': '2.25'}                                                                                                                      
{'loss': '0.5576', 'grad_norm': '3.508', 'learning_rate': '2.75e-05', 'epoch': '2.5'}                                                                                                                    
{'loss': '0.4296', 'grad_norm': '5.219', 'learning_rate': '2.5e-05', 'epoch': '2.75'}                                                                                                                    
{'loss': '0.7099', 'grad_norm': '8.759', 'learning_rate': '2.25e-05', 'epoch': '3'}                                                                                                                      
{'eval_loss': '0.7414', 'eval_accuracy': '0.25', 'eval_runtime': '0.9252', 'eval_samples_per_second': '4.324', 'eval_steps_per_second': '2.162', 'epoch': '3'}                                           
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.28it/s]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.5113', 'grad_norm': '3.588', 'learning_rate': '2e-05', 'epoch': '3.25'}                                                                                                                      
{'loss': '0.6288', 'grad_norm': '7.565', 'learning_rate': '1.75e-05', 'epoch': '3.5'}                                                                                                                    
{'loss': '0.4974', 'grad_norm': '4.67', 'learning_rate': '1.5e-05', 'epoch': '3.75'}                                                                                                                     
{'loss': '0.2843', 'grad_norm': '3.956', 'learning_rate': '1.25e-05', 'epoch': '4'}                                                                                                                      
{'eval_loss': '0.7327', 'eval_accuracy': '0.5', 'eval_runtime': '0.8973', 'eval_samples_per_second': '4.458', 'eval_steps_per_second': '2.229', 'epoch': '4'}                                            
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.35s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
{'loss': '0.5085', 'grad_norm': '5.052', 'learning_rate': '1e-05', 'epoch': '4.25'}                                                                                                                      
{'loss': '0.4048', 'grad_norm': '4.321', 'learning_rate': '7.5e-06', 'epoch': '4.5'}                                                                                                                     
{'loss': '0.4052', 'grad_norm': '4.311', 'learning_rate': '5e-06', 'epoch': '4.75'}                                                                                                                      
{'loss': '0.3483', 'grad_norm': '4.984', 'learning_rate': '2.5e-06', 'epoch': '5'}                                                                                                                       
{'eval_loss': '0.7277', 'eval_accuracy': '0.5', 'eval_runtime': '0.9101', 'eval_samples_per_second': '4.395', 'eval_steps_per_second': '2.198', 'epoch': '5'}                                            
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.44s/it]
{'train_runtime': '65.47', 'train_samples_per_second': '0.611', 'train_steps_per_second': '0.305', 'train_loss': '0.5601', 'epoch': '5'}                                                                 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [01:05<00:00,  3.27s/it]
C:\Users\NT551XED\anaconda3\envs\py312\Lib\site-packages\torch\utils\data\dataloader.py:752: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
  super().__init__(loader)
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  4.47it/s]
평가 결과: {'eval_loss': 0.7277388572692871, 'eval_accuracy': 0.5, 'eval_runtime': 0.9152, 'eval_samples_per_second': 4.371, 'eval_steps_per_second': 2.185, 'epoch': 5.0}
Writing model shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.18s/it]
내 모델 저장 완료:  ./my_local_model
"""