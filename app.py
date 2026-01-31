import streamlit as st

st.set_page_config(page_title="Test", page_icon="📱")

st.title("iOS Test")
st.write("If you see this, Streamlit is working!")

if st.button("Click me"):
    st.success("Button works!")