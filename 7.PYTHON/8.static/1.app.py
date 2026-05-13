from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def user():
    return send_from_directory('static', 'user.html') # static 폴더에서 user.html 파일을 찾아서 응답 (가공하지 않고 그대로 줌)

if __name__ == '__main__':
    # app.run(port=5000,debug=True)
    app.run(debug=True)