# pip install Flask-Session
from flask import Flask, render_template, request, redirect, url_for
from flask import session # 서버측에 세션을 저장하기 위한 확장 클래스

# Session은 더 이상 안함 -> 실무적으로는 이게 DB에서 대체함

# url_for() 는 Flask에서 함수 이름을 이용해서 URL 주소를 만들어주는 함수입니다.
# URL 주소 = '/dashboard'
# 함수 이름 = 'welcome'
# return redirect(url_for('welcome'))  == > return redirect('/dashboard') 같은 의미

app = Flask(__name__)
app.secret_key = 'my-random-key'

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]

@app.route('/dashboard')
def welcome():
    user =session.get('user') # 세션 정보에서 사용자 읽어온다
    return render_template('dashboard.html', name=user['name'])

@app.route('/', methods=['GET'])
def home():
    if session.get('user'):
        return redirect(url_for('welcome')) # 로그인한 사용자가 홈에 오면 대시보드로 리다이렉트
    
    # 로그인이 한적이 없을떄, 그냥 첫 방문    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    if request.method == 'POST':
        # 1. 요청에서 id/pw 가져온다
        # id=입력한 아이디, pw=입력한 패스워드
        id = request.form.get('id') # name="id"인 input에서 가져온다
        pw = request.form.get('pw') # name="pw"인 input에서 가져온다

        # 2. user db에서 이 사용자 매칭한다
        user = next((u for u in users if u['id'] == id and u['pw'] == pw), None) # 매칭되는 사용자 찾기, 없으면 None

        # 3. 사용자가 있으면?
        # 로그인에 성공하면 쿠키에 저장 쿠키에서 지워질 때 까지 로그인 상태 유지("Login successful") 삭제되면 원래대로('index.html' 페이지)
        if user:
            session['user'] = user # 로그인한 사용자를 세션에 저장한다.
            error = None
            return redirect(url_for('welcome')) # 로그인 성공하면 대시보드로 리다이렉트
        else:
            error = "Invalid ID or password"

        return render_template('index.html', error=error)

# 1. 사용자가 비밀번호 바꾸는 기능을 추가한다
# 1-1. method를 POST로 확장
# 1-2. users 안에서 나의 비번을 바꾼다.
# 1-3. 성공적으로 변경되면 나의 profile에서 확인한다.
# 1-4. '비밀번호 변경'을 눌렀을때 성공적으로 변경되었음을 알려준다.(사용자 피드백)
@app.route('/profile', methods=['GET', 'POST'])    
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('home')) # 로그인 안됐으면 로그인 페이지로 강제 이동
    
    if request.method == 'POST':
        new_pw = request.form.get('new_pw')
        # users 리스트에서 현재 로그인한 사용자의 비밀번호를 변경한다.
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw
                session['user'] = u # 세션정보를 구 -> 신 버전으로 갱신 (이래야 반영)
    
                message = "비밀번호가 성공적으로 변경되었습니다."
                # return redirect(url_for('profile')) # 변경된 정보가 반영된 프로필 페이지로 리다이렉트
                return render_template('profile.html', user=u, message=message) # 변경된 사용자 정보와 메시지를 프로필 페이지로 전달
            
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None) # 세션에서 사용자 정보 제거  None은 키가 없을째, 즉 로그아웃 두번 했을때 오류 방지용
    return redirect(url_for('home')) # 로그아웃 후 홈으로 리다이렉트

if __name__ == "__main__":
    app.run(debug=True)