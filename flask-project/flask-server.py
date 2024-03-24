from flask import Flask, request, jsonify
from RecommendBooks import *

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

@app.route('/firstCall', methods=['POST'])
def handle_post_request():
    data = request.get_json()  # Get JSON data from the request body
    firstBookCall()
    print("YAY")
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)