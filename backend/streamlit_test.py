import streamlit as st
import requests

# Initialize conversation history in session state
if 'history' not in st.session_state:
    st.session_state.history = []

# Title for your app
st.title("API Request Test")

# Text input box where the user can enter a value
user_input = st.text_input("Enter a value:", "default value")

# Button to send the request
if st.button("Send Request"):
    # Sending request to the Flask API with the user input and history
    response = requests.get("http://127.0.0.1:5000/rand", params={"input": user_input, "conversation_history": st.session_state.history})

    # Update history based on the response
    if response.ok:
        st.session_state.history.append(user_input)
        st.session_state.history.extend(response.json().get('conversation_history', []))
        st.success("Response from API: " + response.text)
    else:
        st.error("Failed to get response from API")
