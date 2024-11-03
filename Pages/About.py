import streamlit as st

# Set page configuration for a futuristic AI theme
st.set_page_config(
    page_title="About - ChatGPT Clone",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background color and font styling */
        .main {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: Arial, sans-serif;
        }
        /* Title styling */
        .title {
            color: #58a6ff;
            font-size: 2.5em;
            text-align: center;
        }
        /* Subtitle styling */
        .subtitle {
            color: #8b949e;
            text-align: center;
            font-size: 1.2em;
        }
        /* Paragraph styling */
        .description {
            font-size: 1em;
            line-height: 1.5;
            margin: 20px 0;
        }
        /* Accent colors for important text */
        .highlight {
            color: #39d353;
            font-weight: bold;
        }
        /* Footer */
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown("<h1 class='title'>🤖 About ChatGPT Clone</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>An AI-Powered Assistant for Conversational AI Enthusiasts</p>", unsafe_allow_html=True)

# Description with enhanced styling
st.markdown("""
<div class='description'>
Welcome to the <span class='highlight'>ChatGPT Clone</span>, an interactive and intelligent AI assistant built on 
OpenAI's <span class='highlight'>GPT-3.5-turbo</span> model. This app brings you the capabilities of natural language processing
to create a seamless, conversational experience.

### Why This Clone?
This project is more than just a chatbot. It allows you to:
- **Experiment** with cutting-edge AI technology.
- **Learn** about conversational AI and how it works.
- **Interact** in real-time with an AI model that adapts to your inputs.

### Powered by OpenAI
Leveraging the powerful **GPT-3.5-turbo** model, this clone provides responses that are contextually aware, helpful, and engaging.
Get ready to explore the possibilities of AI conversations and discover how machines can understand and respond to human language.

### How It Works
Our chatbot uses OpenAI's API to generate responses based on your input, creating a unique and personalized conversation each time.

### Whisper Integration
In addition to chatting, this application also features an integrated **Whisper** model for voice-to-text capabilities. This allows users to:
- **Transcribe** spoken language into text in real-time.
- **Understand** and interact with the AI without typing.
- **Enhance** accessibility for users with different needs.

### Vision Integration
With the **Vision** functionality, you can describe images and receive generated images based on your textual input. This feature allows users to:
- **Generate visuals** from textual descriptions.
- **Explore** the relationship between text and imagery in AI.
- **Engage** in creative applications of AI by seeing how it interprets descriptions.

</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; color: #8b949e; margin-top: 30px;'>
    Made with 💻 and 🤖  leveraging OpenAI technology.
</div>
""", unsafe_allow_html=True)