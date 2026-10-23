import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="DITE Study Buddy")
st.title("DITE Study Buddy - AI Notes Summarizer")

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

notes = st.text_area("Paste your notes here:")

if st.button("Generate Summary"):
    if notes:
        with st.spinner("Generating summary..."):
            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                prompt = f"Summarize this text in 5 easy points and make 3 MCQs: {notes}"
                result = model.generate_content(prompt)
                st.success("Here is your summary:")
                st.write(result.text)
            except Exception as e:
                st.error(f"Model error, trying backup model... {e}")
                model = genai.GenerativeModel("gemini-pro")
                result = model.generate_content(prompt)
                st.write(result.text)
    else:
        st.warning("Please paste some notes first.")
