
import streamlit as st
import requests

st.set_page_config(page_title="ToS Summarizer", layout="centered")
st.title("📄 Terms of Service Summarizer")

st.markdown("Enter the Terms of Service (ToS) text below and click **Summarize** to get a plain-language summary.")

tos_text = st.text_area("Paste Terms of Service text here", height=300)

if st.button("Summarize"):
    if tos_text.strip():
        st.write("✍️ Generating summary...")
        # Placeholder summary logic (replace with actual model call)
        summary = "This is a placeholder summary of the provided Terms of Service."
        st.success("✅ Summary Generated:")
        st.write("summary", summary, height=300)
    else:
        st.warning("⚠️ Please enter some text before summarizing.")
