import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR API KEY'
st.title("Whisper - Speech to Text")

# Upload audio file
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file is not None:
    # Convert speech to text
    st.audio(audio_file, format="audio/wav")
    st.write("Processing...")

    # Use OpenAI's Whisper model for transcription
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
    )
    st.write("Transcription:")
    st.write(response['text'])