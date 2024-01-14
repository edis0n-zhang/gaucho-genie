from flask import Flask, request, jsonify
import random
import chatbot_query

app = Flask(__name__)

@app.route("/rand")
def hello():
    # Access the query parameters
    user_input = str(request.args.get("input", ""))
    conversation_history = str(request.args.get("conversation_history", ""))

    result = chatbot_query.process_query(user_input, conversation_history)

    # Return a JSON response
    return {
        "output": str(result),
        "conversation_history": conversation_history
    }

if __name__ == "__main__":
    app.run(debug=True)
