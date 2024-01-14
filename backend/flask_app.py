from flask import Flask, request, jsonify, send_from_directory
import random
import chatbot_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/get_response")
def get_response():
    print("GET request received")
    # Access the query parameters
    user_input = str(request.args.get("input", ""))
    conversation_history = str(request.args.get("conversation_history", ""))

    result, conversation_history = chatbot_query.process_query(user_input, conversation_history)

    # Return a JSON response
    return jsonify({
        "output": str(result),
        "conversation_history": conversation_history
    })

if __name__ == "__main__":
    app.run(debug=True)
