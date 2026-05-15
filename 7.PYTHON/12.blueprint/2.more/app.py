from flask import Flask, render_template

# user_routes.py와 admin_routes.py에서 각각 Blueprint 객체를 만들어서 라우팅을 정의한 뒤, app.py에서 이 Blueprint들을 등록해서 사용하는 방식으로 구조를 개선해보자
from routes.user.user_routes import user_blueprint
from routes.admin.admin_routes import admin_blueprint
from routes.product.product_routes import product_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(product_blueprint, url_prefix='/product')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
