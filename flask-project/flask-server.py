from flask import Flask

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

@app.route('/post', methods=['POST'])
def handle_post_request():
    data = request.get_json()  # Get JSON data from the request body
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400  # Bad request

    # Assuming the JSON data contains a 'message' field
    if 'message' not in data:
        return jsonify({'error': 'No message provided in JSON data'}), 400  # Bad request

    message = data['message']
    # Here you can perform any processing with the received message
    # For simplicity, let's just echo back the message
    response = {'echo': message}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)