import streamlit as st

# Set a custom CSS style for the AI-inspired color theme
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #1b1e3c;  /* Dark purple background */
        color: #e0e0e0;  /* Light gray text */
    }
    
    /* Sidebar customization */
    .sidebar .sidebar-content {
        background-color: #212946;  /* Dark blue-gray sidebar */
        color: #a0a8c5;
    }
    
    /* Titles and headers */
    h1, h2, h3 {
        color: #5db8fe;  /* Electric blue headers */
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #28a745;  /* Neon green button background */
        color: #ffffff;
        border-radius: 8px;
        font-size: 16px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1f8f6e; /* Darker green on hover */
    }
    
    /* Chat message bubbles */
    .user-bubble {
        background-color: #2c2f48;
        border-radius: 12px;
        padding: 10px;
        color: #a0a8c5;
        margin-bottom: 5px;
    }
    .bot-bubble {
        background-color: #3c3f5e;
        border-radius: 12px;
        padding: 10px;
        color: #a0a8c5;
        margin-bottom: 5px;
    }
    
    /* Footer */
    footer {
        font-size: 0.8em;
        color: #a0a8c5;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with AI-inspired look
st.sidebar.title("🤖 AI Chatbot")
st.sidebar.write("Navigate through the chatbot app with a high-tech look.")

# Title and description
st.title("💬 ChatGPT AI Clone")
st.write("Experience an advanced AI chatbot with a sleek design.")
st.write('How to interact with the model , below shown example!.')

# Sample message bubbles with custom CSS classes
def user_message(msg):
    st.markdown(f"<div class='user-bubble'><strong>You:</strong> {msg}</div>", unsafe_allow_html=True)

def bot_message(msg):
    st.markdown(f"<div class='bot-bubble'><strong>Bot:</strong> {msg}</div>", unsafe_allow_html=True)

# Display chat bubbles
user_message("How can AI help me today?")
bot_message("I'm here to assist you with all your questions.")

# Button to refresh chat
if st.button("🔄 Refresh Chat"):
    st.write("Chat refreshed")

# Footer with AI-inspired color
st.markdown("""
    <hr>
    <footer>
        <p>Powered by OpenAI | <a href='https://www.openai.com' style='color:#5db8fe;'>Visit OpenAI</a> | <a href='https://github.com/username/repo' style='color:#5db8fe;'>GitHub</a></p>
    </footer>
""", unsafe_allow_html=True)