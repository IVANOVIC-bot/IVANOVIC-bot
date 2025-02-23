from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    
    # This is where you can process the message and generate a response
    response = generate_response(message)
    
    return jsonify({"response": response})

def generate_response(message):
    # Placeholder function for generating a response
    return f"You said: {message}"

if __name__ == '__main__':
    app.run(debug=True)