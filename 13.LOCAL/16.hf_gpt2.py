from transformers import pipeline
from transformers import AutoTokenizer

# GPT-2 모델
model_name="gpt2"

text_gnenerator = pipeline("text-generation", model=model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

result = text_gnenerator(
    "Once upon a time, ",
    max_length=50,
    truncation=True,
    pad_token_id=tokenizer.eos_token_id)[0]

print(result["generated_text"])
