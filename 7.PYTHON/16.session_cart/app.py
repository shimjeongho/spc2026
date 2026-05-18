from flask import Flask, render_template, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello1234'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)  # 세션 유지 시간 (초)

items = [
    {'id': 'item1', 'name': '햄버거', 'price': 3000},
    {'id': 'item2', 'name': '핫도그', 'price': 2000},
    {'id': 'item3', 'name': '콜라', 'price': 1500},
]

# 1. 상품 보여주기
# 2. 카트에 추가 시 a태그를 잘 확장해서 /add-to-cart 곳을 호출
# 3.

@app.route('/')
def index():
    return render_template('product.html', items=items) # 여기 상품 채워넣기

@app.route('/add-to-cart/<item_id>')
def add_to_cart(item_id):
    print("장바구니에 담을 상품: ", item_id)
    if 'cart' not in session:
        session['cart'] = {}  # 세션에 장바구니가 없으면 빈 딕셔너리로 초기화

    if item_id in session['cart']:
        session['cart'][item_id] += 1  # 이미 장바구니에 있으면 수량 증가
    else:
        # 장바구니에 담을 상품이 실제로 존재하는가?
        session['cart'][item_id] = 1 

    print(session['cart'])  # 장바구니 상태 출력
    session.modified = True  # 세션 데이터가 수정되었음을 Flask에 알림 (이거 없으면 세션이 업데이트 안됨 한번만 됨)

    return redirect(url_for('index')) # 상품 페이지로 리다이렉트

@app.route('/cart')
def view_cart():
    cart_items = {}
    total_price = 0

    # {} -> 초기값을 널어줘야 for문에서 에러 안남
    for item_id, quantity in session.get('cart', {}).items():
        item = next((i for i in items if i['id'] == item_id), None)
        cart_items[item_id] = {
            'name': item['name'],
            'quantity': quantity,
            'price': item['price']
        }
        total_price += item['price'] * quantity

    return render_template('cart.html', cart_items=cart_items, total_price=total_price) # 여기에 장바구니에 담긴 상품 채워넣기

if __name__ == "__main__":
    app.run(debug=True)