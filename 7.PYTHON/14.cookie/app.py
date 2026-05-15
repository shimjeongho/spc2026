from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set-cookie")
def set_cookie():
    # 응답 메시지
    resp = make_response("COOKIE has been set!!")
    # 실제로 가져감
    resp.set_cookie("my_edu", "spc2026")

    return resp

@app.route("/get-cookie")
def get_cookie():
    cookie = request.cookies.get("my_edu")
    print(cookie)

    return f"안녕, {cookie} 야" # 안녕, spc2026 야

if __name__ == "__main__":
    app.run(debug=True)