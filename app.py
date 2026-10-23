import streamlit as st
from google import genai

st.title("DITE Study Buddy")
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

notes = st.text_area("Paste notes:")

if st.button("Generate"):
    if notes:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=notes
        )
        st.write(response.text)
