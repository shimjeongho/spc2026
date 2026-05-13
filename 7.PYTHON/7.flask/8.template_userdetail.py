from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-456-7890'},
    {'name': 'Bob', 'age': 30, 'phone': '123-555-7890'},
    {'name': 'Charlie', 'age': 27, 'phone': '123-777-7890'},
    {'name': 'David', 'age': 25, 'phone': '123-888-7890'}
]

@app.route('/')
def index():
    final_html = render_template('users_detail.html', users=users)
    print(final_html)
    return final_html

if __name__ == '__main__':
    app.run(debug=True)

"""
<html>
    <head>
        <title>마이 타이틀</title>
    </head>
    <body>
        <h1>사용자 명단</h1>
        <ul>
            
            <li>사용자 이름 : Alice</li>
            <ul>
                <li>나이 : 25</li>
                <li>전화번호 : 123-456-7890</li>
            </ul>
            
            <li>사용자 이름 : Bob</li>
            <ul>
                <li>나이 : 30</li>
                <li>전화번호 : 123-555-7890</li>
            </ul>
            
            <li>사용자 이름 : Charlie</li>
            <ul>
                <li>나이 : 27</li>
                <li>전화번호 : 123-777-7890</li>
            </ul>
            
            <li>사용자 이름 : David</li>
            <ul>
                <li>나이 : 25</li>
                <li>전화번호 : 123-888-7890</li>
            </ul>
            
        </ul>
    </body>
</html>
"""