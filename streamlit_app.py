import streamlit as st
import google.generativeai as genai

# 🔐 Configure Gemini API
genai.configure(api_key="AIzaSyDSivQyHMMzni1bh_VpL8w7cyXAVLMSwr8")

# 🎓 Model
model = genai.GenerativeModel("gemini-2.5-flash")

# UI
st.title("ProfessorGPT App (Powered by Gemini)")
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
