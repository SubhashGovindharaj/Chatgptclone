import streamlit as st

st.title("Settings")

# Select chatbot personality
st.subheader("Chatbot Personality")
personality = st.selectbox(
    "Choose a personality for the chatbot:",
    ("Helpful", "Friendly", "Sarcastic", "Professional")
)
st.write(f"Personality set to: {personality}")

# Set chat language (for future multilingual support)
st.subheader("Chat Language")
language = st.selectbox(
    "Choose language for the chatbot:",
    ("English", "Spanish", "French", "German")
)
st.write(f"Language set to: {language}")

# Customize Model (for users with access to GPT-4, for instance)
st.subheader("Model")
model_choice = st.radio("Choose model version:", ("gpt-3.5-turbo", "gpt-4"))
st.write(f"Model set to: {model_choice}")

# Save settings to session state
st.session_state['personality'] = personality
st.session_state['language'] = language
st.session_state['model_choice'] = model_choice