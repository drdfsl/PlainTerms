import streamlit as st
import fitz  # PyMuPDF
import openai

# Load your OpenAI API key securely from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="PlainTerms", layout="centered")
st.title("PlainTerms")
st.write("Upload a Terms of Service PDF and get a plain English summary.")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def generate_summary(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You summarize legal documents into plain, simple English."},
                {"role": "user", "content": f"Summarize this Terms of Service in plain English:\n\n{text}"}
            ],
            temperature=0.5
        )
        summary = response["choices"][0]["message"]["content"].strip()
        return summary
    except Exception as e:
        return f"Error generating summary: {e}"

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = generate_summary(text)
            st.success("Summary generated!")
            st.text_area("Plain English Summary", summary, height=400)

            # Add download option
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

