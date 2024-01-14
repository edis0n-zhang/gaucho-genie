import streamlit as st
import requests

conversation_history = str()

# Title for your app
st.title("API Request Test")

# Text input box where the user can enter a value
user_input = st.text_input("Enter a value:", "default value")

# Button to send the request
if st.button("Send Request"):
    # Sending request to the Flask API with the user input and history
    response = requests.get("http://127.0.0.1:5000/rand", params={"input": user_input, "conversation_history": conversation_history})

    # Update history based on the response
    if response.ok:
        response_json = response.json()
        conversation_history = response_json.get('conversation_history', "")
        st.success("Response from API: " + response.text)
    else:
        st.error("Failed to get response from API")
