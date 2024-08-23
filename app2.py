import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

# Function to generate image
def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.content

st.title("Welcome to the Image Generator")

# Input for the user's prompt
prompt = st.text_input("Enter your prompt")

# Button to generate the image
if st.button("Generate Image"):
    image_bytes = generate_image(prompt)
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption=f"Generated Image for prompt: {prompt}")
