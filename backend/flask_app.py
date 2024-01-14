from flask import Flask, request, jsonify
import random
import chatbot_query

app = Flask(__name__)

@app.route("/rand")
def hello():
    # Access the query parameters
    user_input = request.args.get("input", "")
    conversation_history = request.args.getlist("conversation_history")
    
    result, updated_history = chatbot_query.process_query(user_input, conversation_history)

    # Return a JSON response
    return jsonify({
        "output": str(result),
        "conversation_history": str(updated_history)
    })

if __name__ == "__main__":
    app.run(debug=True)
