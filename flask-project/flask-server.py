from flask import Flask, request, jsonify
import json
from RecommendBooks import *

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

@app.route('/firstCall', methods=['POST'])
def handle_post_request_1():
    data = request.get_json()  # Get JSON data from the request body
    reccs = firstBookCall()
    print("IT GOT CALLED")
    print(reccs)
    return reccs

@app.route('/recommend', methods=['POST'])
def handle_post_request_2():
    data = request.get_json()  # Get JSON data from the request body
    choices = json.loads(data)
    genres = getGenres(choices)
    reccs = getBookRecs(genres)
    print("It got called")
    print(reccs)
    return reccs

if __name__ == "__main__":
    app.run(port=5000, debug=True)