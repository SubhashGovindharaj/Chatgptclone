import streamlit as st
import openai
import numpy as np
import soundfile as sf
import tempfile
from pydub import AudioSegment
# Set your OpenAI API key
openai.api_key = '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'





st.title("Audio Transcriber and Summarizer")

audio_files = st.file_uploader("Upload audio files (WAV or MP3)", type=["wav", "mp3"], accept_multiple_files=True)

if audio_files:
    for audio_file in audio_files:
        st.audio(audio_file, format="audio/wav")
        st.write("Processing...")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            if audio_file.type == "audio/mp3":
                sound = AudioSegment.from_file(audio_file, format="mp3")
                sound.export(tmp_file.name, format="wav")
            else:
                tmp_file.write(audio_file.read())

            # Transcribe audio
            with open(tmp_file.name, "rb") as audio_file:
                response = openai.Audio.transcribe(model="whisper-1", file=audio_file)

            transcription = response['text']
            st.write("Transcription:")
            st.write(transcription)

            # Summarize transcription
            summary_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Summarize this text: {transcription}"}]
            )
            summary = summary_response['choices'][0]['message']['content']
            st.write("Summary:")
            st.write(summary)

            # Optionally, allow downloads
            st.download_button("Download Transcription", transcription, "transcription.txt")
            st.download_button("Download Summary", summary, "summary.txt")