import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

model = 'claude-opus-4-8'

prompt = "12 x 13을 어떻게 푸는지 단계별로 설명해줘"

with client.messages.stream(
    model=model,
    max_tokens=2000,
    thinking={"type":"adaptive", "display": "summarized"},
    messages=[{"role":"user", "content": prompt}]
)as stream:
    for event in stream:
        if event.type == "content_block_start":
            if event.content_block.type == "thinking":
                print("\n[생각] ", end="", flush=True)
            elif event.content_block.type == "text":
                print("\n\n[답변] ", end="", flush=True)
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                print(event.delta.thinking, end="", flush=True)
            elif event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)
print()

"""
[생각]  The user is asking for a step-by-step breakdown of how to multiply 12 by 13, and they want the explanation in Korean.

[답변] # 12 × 13 풀이 방법

## 방법 1: 분배법칙 이용하기 (가장 추천)

13을 **10과 3으로 나누어** 계산하는 방법이에요.

**1단계:** 13을 10 + 3으로 분리합니다
$$12 \times 13 = 12 \times (10 + 3)$$

**2단계:** 각각 곱합니다
- 12 × 10 = **120**
- 12 × 3 = **36**

**3단계:** 두 결과를 더합니다
$$120 + 36 = \boxed{156}$$

---

## 방법 2: 세로셈 (전통적인 곱셈)

```
      1 2
   ×  1 3
   -------
      3 6    ← 12 × 3
    1 2 0    ← 12 × 10
   -------
    1 5 6
```

**1단계:** 12 × 3 = 36 (일의 자리 곱셈)
**2단계:** 12 × 10 = 120 (십의 자리 곱셈)
**3단계:** 36 + 120 = **156**

---

## 정답: **12 × 13 = 156**

💡 **꿀팁:** 두 자리 수 곱셈은 **방법 1처럼 하나의 수를 쪼개서** 계산하면 암산하기 훨씬 쉬워요!

더 궁금한 점 있으면 물어보세요! 😊
"""