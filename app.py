import streamlit as st

st.title('Cold Email Generator ✉️')
url_input = st.text_input("Enter a URL",value="")
submit_button = st.button("Submit")

if url_input:
    st.write(f"Processing URL: {url_input}")
