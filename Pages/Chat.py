import streamlit as st
import openai
from streamlit_chat import message

# Set your OpenAI API key
openai.api_key = 'Your API KEY'

# Title for the Chat page
st.title("Chat with LULU")


# Initialize conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Function to get response from OpenAI
def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        bot_response = response['choices'][0]['message']['content'].strip()
        return bot_response
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, I encountered an error while generating a response."

# Callback for handling user input
def handle_user_input():
    user_input = st.session_state["user_input"]
    if user_input:
        st.session_state.conversation.append({"role": "user", "content": user_input})
        bot_response = get_response(user_input)
        st.session_state.conversation.append({"role": "bot", "content": bot_response})
        st.session_state.user_input = ""

# User input field with callback
st.text_input("You:", placeholder="Type your message here...", key="user_input", on_change=handle_user_input)

# Display conversation history
for i, chat in enumerate(st.session_state.conversation):
    if chat["role"] == "user":
        message(chat["content"], is_user=True, key=f"user_{i}")
    else:
        message(chat["content"], key=f"bot_{i}")
        # Display the developer signature below the bot response
        st.markdown("<p style='color: gray; font-size: 0.9em;'>Developed by Subhash Govindaraj</p>", unsafe_allow_html=True)