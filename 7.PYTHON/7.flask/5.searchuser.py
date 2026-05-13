from flask import Flask
from flask import jsonify 
from flask import request 

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-456-7890'},
    {'name': 'Bob', 'age': 30, 'phone': '123-555-7890'},
    {'name': 'Charlie', 'age': 27, 'phone': '123-777-7890'},
    {'name': 'David', 'age': 25, 'phone': '123-888-7890'}
]   

@app.route('/users')    
def search_users():

    name = request.args.get('name')
    age = request.args.get('age', type=int)
    phone = request.args.get('phone')
    # 쿼리 파라미터로 name, age, phone로 검색해서 결과를 반환
    
    result = users

    if name:
        result = [u for u in users if name.lower() == u['name'].lower()]

    if age:
        result = [u for u in result if  int(age) == u['age']] 

    # 기능 추가 - 국번으로 조회하기 (앞글자 startswith로)
    if phone:
        # result = [u for u in result if  phone == u['phone']]
        result = [u for u in result if u['phone'].startswith(phone)]


    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)