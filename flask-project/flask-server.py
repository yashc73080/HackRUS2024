# from flask import Flask, request, jsonify
# from RecommendBooks import *

# app = Flask(__name__)

# @app.route('/flask', methods=['GET'])
# def index():
#     return "Flask server"

# @app.route('/firstCall', methods=['POST'])
# def handle_post_request_1():
#     reccs = request.data.decode('utf-8').split(',')
#     print(reccs)
#     return reccs

# @app.route('/recommend', methods=['POST'])
# def handle_post_request_2():
#     choices = request.data.decode('utf-8').split(',')
#     genres = getGenres(choices)
#     reccs = getBookRecs(genres)
#     print(reccs)
#     return reccs

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
import ast  # Import Abstract Syntax Trees module to safely evaluate string expressions
from RecommendBooks import firstBookCall, getGenres, getBookRecs

app = Flask(__name__)

@app.route('/firstCall', methods=['GET'])
def handle_first_call():
    books = firstBookCall()
    return jsonify(books)

@app.route('/recommend', methods=['POST'])
def handle_recommendation():
    try:
        # Assuming the body is a string that can be safely evaluated as a list
        choices_str = request.data.decode('utf-8')
        choices = ast.literal_eval(choices_str)  # Safely evaluate string to Python literal

        if not isinstance(choices, list) or not all(isinstance(item, int) for item in choices):
            raise ValueError("Invalid input format. Expected an array of integers.")

    except (ValueError, SyntaxError) as e:
        return f"Error parsing input: {e}", 400

    genres = getGenres(choices)
    reccs = getBookRecs(genres)
    return jsonify(reccs)

if __name__ == "__main__":
    app.run(port=5000, debug=True)