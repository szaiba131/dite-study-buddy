import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="DITE Study Buddy")
st.title("DITE Study Buddy - AI Notes Summarizer")
st.write("Paste your notes and get an easy summary in seconds.")

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

notes = st.text_area("Paste your notes here:")

if st.button("Generate Summary"):
    if notes:
        with st.spinner("Generating summary..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Summarize this text in 5 easy points and make 3 MCQs: {notes}"
            result = model.generate_content(prompt)
            st.success("Here is your summary:")
            st.write(result.text)
    else:
        st.warning("Please paste some notes first.")
