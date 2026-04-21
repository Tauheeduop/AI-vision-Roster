import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("Tech Lead Roaster")
uploaded_file = st.file_uploader("Upload your setup or code...", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Analyzing your disaster...")

    if st.button("Roast Me!"):
        prompt = "You are a savage Senior Tech Lead. Roast this technical setup or image in professional English. Focus on bottlenecks, poor ergonomics, or bad practices. Keep it short and brutal."
        
        response = model.generate_content([prompt, img])
        st.error(response.text)