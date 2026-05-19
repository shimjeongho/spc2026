from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import request

app = Flask(__name__)
app.secret_key = "abcd1234"

items = [
    {'id': 1, 'name': 'apple', 'price': 1000},
    {'id': 2, 'name': 'banana', 'price': 2000},
    {'id': 3, 'name': 'cherry', 'price': 3000},
]

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]

# 홈
@app.route("/")
def home():

    return render_template("index.html")


# 상품 목록
@app.route("/product")
def product():

    message = session.pop("message", None)

    return render_template(
        "product.html",
        items=items,
        message=message
    )


# 로그인
@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        # 사용자가 입력한 값
        userid = request.form.get('userid')
        password = request.form.get('password')

        # users 에서 회원 찾기
        user = next((u for u in users if u['id'] == userid and u['pw'] == password), None)

        # 로그인 성공
        if user:
            session['user'] = user
            return redirect(url_for('success'))

        # 로그인 실패
        else:
            error = "아이디 또는 비밀번호 오류"
            return render_template("login.html",error=error)

    # GET 요청
    return render_template("login.html")

# 로그인 성공 화면
@app.route("/success")
def success():

    user = session.get('user')

    if not user:
        return redirect(url_for('login'))

    return render_template("success.html", user=user['name'])

# 로그아웃
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for('home'))


# 장바구니 담기
@app.route("/add_cart/<int:item_id>")
def add_cart(item_id):

    # 로그인 안 되어 있으면
    if 'user' not in session:

        session['message'] = '로그인 후 이용 가능합니다.'

        return redirect(url_for('product'))

    # 로그인 되어 있으면
    return f"{item_id}번 상품 담기 완료!"


if __name__ == "__main__":
    app.run(debug=True)