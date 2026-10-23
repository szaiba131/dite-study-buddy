import streamlit as st
from google import genai

st.set_page_config(page_title="DITE Study Buddy")
st.title("DITE Study Buddy - AI Notes Summarizer")

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

notes = st.text_area("Paste your notes here:")

if st.button("Generate Summary"):
    if notes:
        with st.spinner("Generating..."):
            try:
                # Naya model jo Google keh raha hai
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Summarize this in 5 easy points and make 3 MCQs: {notes}"
                )
                st.write(response.text)
            except Exception as e:
                # Agar phir bhi error aaye to purana stable model try karo
                st.warning(f"Naya model try fail, purana model use kar raha hun: {e}")
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=f"Summarize this: {notes}"
                )
                st.write(response.text)
    else:
        st.warning("Please paste notes first.")
