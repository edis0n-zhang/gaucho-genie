from flask import Flask, request, jsonify, session
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session management

# [Initialize Pinecone, OpenAI, and other components here...]

# Route for processing queries
@app.route('/query', methods=['POST'])
def process_query():
    if 'conversation_history' not in session:
        session['conversation_history'] = []

    query = request.json.get('query')
    
    # [Perform similarity search and prepare data for language model...]

    # Add query to conversation history
    session['conversation_history'].append(HumanMessage(content=f"{query} \n\n Please answer by utilizing the information provided: \n\n {response_prompt}"))

    # [Generate system response...]

    # Store and return the response
    response = res.content
    session['conversation_history'].append(SystemMessage(content=response))

    # [Manage conversation history length...]

    return jsonify({"response": response})

# Route to reset the conversation
@app.route('/reset', methods=['POST'])
def reset_conversation():
    session.pop('conversation_history', None)
    return jsonify({"message": "Conversation history reset"})

if __name__ == '__main__':
    app.run(debug=True)
