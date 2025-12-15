import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv()

# 🔐 Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found! Please create a .env file with your API key.")
    st.stop()

genai.configure(api_key=api_key)

# 🎓 Model
model = genai.GenerativeModel("gemini-2.5-flash")

# UI
st.title("ProfessorGPT App (Powered by Gemini)")
st.caption("Developed by Vedhas Shinde")
st.divider()

prompt = st.text_input("What do you want to learn?")
gptbutton = st.button("Teach Me")

st.caption("ProfessorGPT will work when you press the button.")
st.divider()

if gptbutton and prompt:
    with st.spinner("ProfessorGPT is thinking..."):
        response = model.generate_content(
            "Teach me the following concept in a simple way:\n" + prompt
        )

    st.subheader("ProfessorGPT's Explanation:")
    st.write(response.text)

