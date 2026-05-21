import requests
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI API KEY 가져오기
openai_api_key = os.getenv('OPENAI_API_KEY')

# 대화 기록 저장 리스트
message = []

# 챗봇 역할 설정
message.append({'role': 'system', 'content': '너는 나를 잘 도와주는 경력 20년차의 작명가야.'})
            

def ask_chatbot(user_input):

    # 사용자 질문 저장
    message.append({'role': 'user', 'content': user_input})

    try:
        # OpenAI API 요청
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            json={
                'model': 'gpt-3.5-turbo',
                'messages': message,
                'temperature' : 1.0,
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {openai_api_key}'     # API 인증
            }
        )

        # 응답 데이터를 JSON 형태로 변환
        data = response.json()

        # 챗봇 응답 내용 추출
        final_response = data['choices'][0]['message']['content']

        # 챗봇 응답 기록 저장
        message.append({'role': 'assistant', 'content': final_response})

        # 최근 대화 20개만 유지
        message = [message[0]] + message[-20:]

    except Exception as e:

        # 오류 발생 시 출력
        print('오류: ', e)

    # 최종 응답 반환
    return final_response


# 첫 실행 테스트
print(ask_chatbot("안녕하세요"))


# 반복 대화
while True:

    # 사용자 입력 받기
    user_input = input("\n당신의질문: ").strip()

    # 종료 명령 처리
    if user_input.lower() in ['quit', 'exit', '종료', '끝']:
        print("대화를 종료합니다. 안녕히 가세요.")
        break

    else:
        print("대화를 생성중입니다. 잠시만 기다려 주세요")

        # 챗봇 응답 출력
        print("챗봇응답: ", ask_chatbot(user_input))

        print('-' * 60)
"""
당신의질문: 나는 고양이 한마리와 강아지 한마리와 사자 한마리가 있어
대화를 생성중입니다. 잠시만 기다려 주세요
챗봇응답:  그렇군요! 각 동물들에게 이름을 지어주고 싶으신가요? 어떤 스타일의 이름을 원하시나요? 예를 들어 귀여운 이름, 멋진 이름, 유니크한 이름 등이 있습니다. 
------------------------------------------------------------

당신의질문: 고양이는 루나 강아지는 루비 사자는 아리라고 할거애
대화를 생성중입니다. 잠시만 기다려 주세요
챗봇응답:  루나, 루비, 아리라는 이름들은 각각 매우 멋지고 매력적인 이름입니다! 동물들이 행복하게 살 수 있도록 좋은 이름을 선택하셨네요. 만약 더 도움이 필요하시다면 언제든지 말씀해주세요. 
------------------------------------------------------------

당신의질문: 그래서 오늘 뭘 먹을까
대화를 생성중입니다. 잠시만 기다려 주세요
챗봇응답:  음식을 선택하는 것은 항상 즐거운 일이죠! 오늘은 어떤 음식이 땡기시나요? 특별히 먹고 싶은 음식이 있거나 요리를 해보고 싶은 음식이 있다면 제안해 드릴 수 있어요. 함께 맛있는 식사를 즐기시길 바랍니다!
------------------------------------------------------------

당신의질문: 그래서 내가 동물이 몇마리 있다고 했지?
대화를 생성중입니다. 잠시만 기다려 주세요
챗봇응답:  네, 당신은 고양이 한마리, 강아지 한마리, 그리고 사자 한마리를 가지고 있다고 말씀하셨습니다. 루나, 루비, 아리라는 이름을 가진 동물들이죠. 어떤 동물들을 가지고 계시는지 잘 기억하고 있습니다. 
"""