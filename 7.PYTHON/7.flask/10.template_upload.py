from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 저장소 설정
app.config['UPLOAD_FOLDER'] = 'uploads'  # 업로드된 파일을 저장할 폴더 경로

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # 폴더가 없으면 생성

def allowed_file(filename):
    # 업로드 허용 확장자 설정
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    # 파일명에 확장자가 있고, 허용된 확장자인지 확인
    # '.' in filename -> 파일명에 확장자가 있는지 확인
    # filename.rsplit('.', 1)[1].lower() -> 파일명에서 확장자 부분을 추출하여 소문자로 변환
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    id = request.form.get('id')
    pw = request.form.get('pw')
    print(f"입력한 ID는 {id}, PW는 {pw}")
    # if id == u['id'] and pw == u['pw']:

    return render_template('login.html', name=id)

# POST로 전달 성공 -> 로그인 성공

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('photo')
    print(file)
    # 우리의 실습상 사용자가 올린 파일명을 그대로 사용하여
    # 실서비스라면 여러 사용자들의 업로드 한 파일명이 필요
    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)  # 파일 저장
        return "파일 받음"
    else:
        return f"지원되지 않은 파일입니다. 파일명: {file.filename}", 400

if __name__ == '__main__':
    app.run(debug=True)