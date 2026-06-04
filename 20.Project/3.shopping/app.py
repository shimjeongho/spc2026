import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory, jsonify, request
from openai import OpenAI

app = Flask(__name__, static_folder="public")

reviews = [] # 사용자들의 댓글을 저장할 변수 (평점과 후기가 함께 들어간다. {'rating': 값, 'comment': 값})

load_dotenv()

openai_api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

#---------------------
# API 라우팅
#---------------------
@app.route('/api/reviews', methods=['POST'])  # POST로 받기
def add_review():
    # review에 저장하기

    data = request.get_json()

    rating = data.get('rating')
    comment = data.get('comment')

    # 유효성 검사
    if not rating or not comment:
        return jsonify({
            'result': 'fail',
            'message': '평점과 후기를 입력해주세요.'
        }), 400
    
    review = {
        'rating' : rating,
        'comment' : comment
    }

    reviews.append(review)

    return jsonify({'message': '리뷰 저장'})  

@app.route('/api/reviews', methods=['GET'])  # GET으로 받기
def get_review():
    # reviews를 가져와서 반환하기
    return jsonify(reviews)

@app.route('/api/ai-summary')  # GET으로 받기
def get_ai_summary():
    # reviews를 가져와서....
    # 여기에서 프롬프트 및 api 호출 코드 작성
    if len(reviews) == 0:
        return jsonify({
            'summary': '현재 리뷰가 없습니다.',
            'average_rating': 'N/A'
        })
    
    # 리뷰 합치기
    review_text =""

    total = 0

    for review in reviews:

        total += int(review['rating'])

        review_text += f"""
            평점: {review['rating']}
            후기: {review['comment']}
        """
    average_rating = round(total / len(reviews), 1)

    # OpenAI    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": '당신은 쇼핑몰 리뷰 요약 AI입니다.'},
            {"role": "user", 'content': f'''
                다음 리뷰들을 2줄로 요약해주세요.

                {review_text}
                '''
            }
        ]
    )

    # 응답을 받아와서 반환한다.
    summary = response.choices[0].message.content
    return jsonify({
        "summary": summary,
        'average_rating': average_rating
    })



#---------------------
# 웹 서비스 라우팅
#---------------------
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)