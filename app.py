import streamlit as st
import google.generativeai as genai

st.title("DITE Study Buddy - AI Notes Summarizer")

api_key = st.text_input("Yahan apni Gemini API Key paste karo:", type="password")
notes = st.text_area("Yahan apne notes paste karo:")

if st.button("Summary Banao"):
    if api_key == "" or notes == "":
        st.warning("Pehle API Key aur Notes dono dalo bhai")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-3.8-flash")
        prompt = f"Is text ko 5 asan points me summarize karo aur 3 MCQs banao: {notes}"
        result = model.generate_content(prompt)
        st.success("Ye raha tumhara summary:")
        st.write(result.text)