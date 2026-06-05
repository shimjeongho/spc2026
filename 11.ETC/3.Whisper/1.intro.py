# whisper (속삭임) 말~~을 기반으로 text로 변환 : STT(Speech-to-text)

# Text-to-speech (tts) ==> GAN

import os
import base64

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def transcribe_audio(file): # 오디오를 설명하시오
    with open(file, "rb") as af:    # af = audio file
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=af,
            response_format="text",  # json, 등등...
            language="ko"   # 한국어
        )
    return transcript

result = transcribe_audio("harvard.wav")
print("결과: ", result)

"""
결과:  오랜 맥주를 마실 때의 짠 냄새가 느껴집니다. 냄새가 빠져나갈 때에는 열이 필요합니다. 차가운 맥주를 마실 때에는 건강과 질감을 회복합니다. 소고기와 잘 어울리는 소고기 피클입니다. 타코즈 알 파스토르는 제 최애입니다. 질감 있는 음식은 핫 크로스 빵입니다.
"""