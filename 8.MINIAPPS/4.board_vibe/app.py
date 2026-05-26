from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)

# Initialize database
database.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/posts', methods=['GET'])
def get_posts():
    try:
        posts = database.get_posts()
        return jsonify({
            'status': 'success',
            'data': posts
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/posts', methods=['POST'])
def add_post():
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'status': 'error',
                'message': '요청 데이터가 없습니다.'
            }), 400
            
        title = data.get('title', '').strip()
        message = data.get('message', '').strip()
        
        if not title:
            return jsonify({
                'status': 'error',
                'message': '제목을 입력해주세요.'
            }), 400
        if not message:
            return jsonify({
                'status': 'error',
                'message': '내용을 입력해주세요.'
            }), 400
            
        new_post = database.add_post(title, message)
        if new_post:
            return jsonify({
                'status': 'success',
                'data': new_post
            }), 201
        else:
            return jsonify({
                'status': 'error',
                'message': '게시글 저장에 실패했습니다.'
            }), 500
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # Running on port 5000, debug=True for easier development
    app.run(host='127.0.0.1', port=5000, debug=True)
