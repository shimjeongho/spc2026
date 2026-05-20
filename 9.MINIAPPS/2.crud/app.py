from flask import Flask, render_template, request, redirect, url_for, session, flash

from datetime import timedelta

import sqlite3

app = Flask(__name__)
app.secret_key = 'hello1234' # 실무적으로는 이런 민감한 credential을 커밋하지 않음

app.permanent_session_lifetime = timedelta(minutes=5)

DATABASE = 'user.sqlite3'   # 나의 파일명

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # 나의 결과를 다 Dict 포맷으로 관리
                                   # row[0] => row['id'] 이런식으로 접근 가능
    return conn

def init_db():
    with app.app_context():        # flask app 초기화 완료된 후
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT 
            )''')
        
        # 기본 계정 추가
        cur.execute("SELECT COUNT(*) AS count FROM users")
        count = cur.fetchone()['count']
        if count == 0:
            cur.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ("user1", "password1", "user1@example.com")) # 실무적으로는 암호화된 비번이 들어간다.
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "password2"))

        conn.commit()

        # 부팅시 계정 정보 출력
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()

        print('-' * 30)
        for row in rows:
            print(row['id'], row['username'], row['password'])  # 이건 다 Row를 Dict 했기 때문에 이름으로 접근 가능
        print('-' * 30)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=["POST"])
def profile_edit():

    if 'user' not in session:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))

    username = session['user']

    # 사용자가 입력한 정보
    password = request.form.get('password')
    email = request.form.get('email')

    conn = get_db_connection()
    cur = conn.cursor()

    # 비밀번호 수정
    if password:
        cur.execute(
            "UPDATE users SET password=? WHERE username=?",
            (password, username)
        )

    # 이메일 수정
    if email:
        cur.execute(
            "UPDATE users SET email=? WHERE username=?",
            (email, username)
        )

    conn.commit()
    conn.close()

    flash("정상적으로 수정되었습니다.")

    return redirect(url_for('profile'))


@app.route('/profile')
def profile():

    username = session.get('user', None)

    if username:

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cur.fetchone()

        conn.close()

        return render_template(
            'profile.html',
            user=user
        )

    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))
    # 내가 한거
    # # 로그인 여부 확인
    # if 'user' not in session:
    #     flash("로그인이 필요합니다.")
    #     return redirect(url_for('login'))

    # username = session['user']

    # conn = get_db_connection()
    # cur = conn.cursor()

    # # 현재 로그인한 사용자 조회
    # cur.execute(
    #     "SELECT * FROM users WHERE username=?",
    #     (username,)
    # )

    # user_data = cur.fetchone()

    # conn.close()

    # if request.method == "POST":

    #     email = request.form.get("email")

    #     cur.execute(
    #         "UPDATE users SET email=? WHERE username=?",
    #         (email, username)
    #     )

    #     conn.commit()

    # return render_template("profile.html", user=user_data)

@app.route('/signin', methods=["GET", "POST"])
def signin():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        conn = get_db_connection()
        cur = conn.cursor()

        # 아이디 중복 검사
        cur.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        existing_user = cur.fetchone()

        if existing_user:
            flash("해당 ID는 사용할 수 없습니다.")
            conn.close()
            return redirect(url_for("signin"))

        # 회원가입
        cur.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )

        conn.commit()
        conn.close()

        flash("회원가입이 완료되었습니다.")
        return redirect(url_for("login"))

    return render_template("signin.html")
        
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", 
        (username, password))
        user_data = cur.fetchone()

        print(username, password)
        print(user_data)
        conn.close()

        if user_data:
            session['user'] = username
            flash("로그인에 성공하였습니다.")
            return redirect(url_for("home"))
        else:
            flash("로그인에 실패하였습니다.")
            return redirect(url_for("login"))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash("성공적으로 로그아웃이 되었습니다.")
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True) # 실무적으로는 꼭 꺼야됨