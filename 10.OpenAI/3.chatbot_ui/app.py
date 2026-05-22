from flask import Flask, request, jsonify, send_from_directory
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__, static_folder='static', static_url_path='') # static 폴더 경로와 그 prefix

history = []


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    chat_message = data.get('chatMessage', '')
    print("사용자 입력값: ", chat_message)
    history.append({'role': 'user', 'content': chat_message})

    #chatgpt에게 물어보기
    get_reply = ask_chatgpt(chat_message)

    history.append({'role': 'assistant', 'content': get_reply})

    # print('>>>>>>>>>>>')
    # print(history)
    # print('<<<<<<<<<<<')

    return jsonify({'reply': get_reply})

# 1. dotenv로 각종 라이브러리랑 롼경변수 불러온다
# 2. client.chat.completions.create() model, messages

def ask_chatgpt(chat_message):

    gpt_ask_message = [
        {'role' : 'system', 'content' : '당신의 나의 질문에 답변을 잘 하는 챗봇입니다.'},
        *history
    ]

    print('>>>>>>>>>>>')
    print("최종 GPT에게 우리가 물어볼 전체 메세지: ", gpt_ask_message)
    print('<<<<<<<<<<<')

    """
    사용자 입력값:  뭘 먹을지 추천해줘
    >>>>>>>>>>>
    최종 GPT에게 우리가 물어볼 전체 메세지:  [{'role': 'system', 'content': '당신의 나의 질문에 답변을 잘 하는 챗봇입니다.'}, {'role': 'user', 'content': '뭘 먹을지 추천해줘'}]
    <<<<<<<<<<<
    ============================================================================================================================================================================
    화면 답변 :
    무엇을 먹을지 고민 중이군요! 당신이 좋아하는 음식 종류나 특정 재료가 있다면 더 구체적인 추천이 가능해요. 예를 들어, 한식, 중식, 양식 중 어떤 것을 선호하시는지, 혹은 면 요리, 볶음 요리, 샐러드 같은 특정 종류가 필요하신지 알려주시면 좋겠습니다!
    """
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages= gpt_ask_message
    )

    return response.choices[0].message.content
if __name__ == "__main__":
    app.run(debug=True)