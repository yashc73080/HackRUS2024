from flask import Flask, request, jsonify
from RecommendBooks import *

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

@app.route('/firstCall', methods=['POST'])
def handle_post_request_1():
    reccs = request.data.split(',')
    print(reccs)
    return reccs

@app.route('/recommend', methods=['POST'])
def handle_post_request_2():
    data = request.data.split(',')
    choices = json.loads(data)
    genres = getGenres(choices)
    reccs = getBookRecs(genres)
    print(reccs)
    return reccs

if __name__ == "__main__":
    app.run(port=5000, debug=True)