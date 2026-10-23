import streamlit as st
from google import genai

st.set_page_config(page_title="DITE Study Buddy")
st.title("DITE Study Buddy - AI Notes Summarizer")

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

notes = st.text_area("Paste your notes here:")

if st.button("Generate Summary"):
    if notes:
        with st.spinner("Generating summary..."):
            prompt = f"Summarize this text in 5 easy points and make 3 MCQs: {notes}"
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            st.success("Here is your summary:")
            st.write(response.text)
    else:
        st.warning("Please paste some notes first.")
