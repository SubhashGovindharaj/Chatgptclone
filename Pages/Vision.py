import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your api key'
st.title("AI Vision Application")

# Input field for the description
description = st.text_input("Enter a description of the image you want to generate:")

if st.button("Generate Image"):
    if description:
        try:
            # Call OpenAI's Image generation model
            response = openai.Image.create(
                prompt=description,
                n=1,
                size="1024x1024"  # You can change the size as needed
            )

            # Get the URL of the generated image
            image_url = response['data'][0]['url']

            # Display the generated image
            st.image(image_url, caption='Generated Image', use_column_width=True)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a description to generate an image.")
