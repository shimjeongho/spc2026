from flask import Flask
from flask import jsonify 
from flask import request 

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')

    page = request.args.get('page', default=1, type=int) # page는 숫자형으로 받겠다. default는 1로 하겠다. (숫자형이 아니면 1로 처리하겠다.)
    

    # ex) http://127.0.0.1:5000/search?q=apple (q = apple)
#     # => {
#           "message": "Your query is apple"
#           }

#     만약 그냥 /search만 했을 경우
#           {
#           "message": "Your query is None"
#           }
# 
#   http://127.0.0.1:5000/search?q=apple&page=10
#         =>
# #         {
#               "message": "Your query is apple and page is 10"
#           }     
    user_input = f"Your query is {query} and page is {page}"

    return jsonify({"message":user_input})


#  http://127.0.0.1:5000/user/alice/post?page=5 
#  {
#    "message": "User is alice and page is 5"
#   }

@app.route('/user/<username>/post')
def show_user_post(username):
    page = request.args.get('page', default=1, type=int) # page는 숫자형으로 받겠다. default는 1로 하겠다. (숫자형이 아니면 1로 처리하겠다.)
    result = f"User is {username} and page is {page}"
    return jsonify({"message": result})


if __name__ == '__main__':
    app.run(debug=True)