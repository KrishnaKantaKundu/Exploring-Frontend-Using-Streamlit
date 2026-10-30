import streamlit as st

st.title("আমার প্রথম অ্যাপ")

name = st.text_input("তোমার নাম কী?")

if name:
    st.write(f"স্বাগতম, {name}!")