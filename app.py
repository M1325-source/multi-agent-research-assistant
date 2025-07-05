
import streamlit as st
from agents.controller import ask_question

st.set_page_config(page_title="Multi-Agent Research Assistant", layout="wide")
st.title("📚 Multi-Agent Research Assistant")

query = st.text_input("Ask a research question across PDFs & web:")

if query:
    with st.spinner("Thinking..."):
        answer = ask_question(query)
        st.markdown("### 🤖 Answer:")
        st.write(answer)
