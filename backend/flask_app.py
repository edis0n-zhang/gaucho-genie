from flask import Flask, request, jsonify
import random
import chatbot_query

app = Flask(__name__)

@app.route("/rand")
def hello():
    # Access the query parameters
    user_input = str(request.args.get("input", ""))

    result = chatbot_query.process_query(user_input)

    # Return a JSON response
    return {"output": str(result)}

if __name__ == "__main__":
    app.run(debug=True)
