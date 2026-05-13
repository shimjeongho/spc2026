from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_names = ["홍길동", "고길동", "김길동", "이길동"]
    final_html = render_template('users.html', names=user_names)
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
            
            <li>홍길동</li>
            
            <li>고길동</li>
            
            <li>김길동</li>
            
            <li>이길동</li>
            
        </ul>
    </body>
</html>
"""