import streamlit as st

st.title("🌳 GreenBox Dashboard")
st.write(
    "View the latest data from our GreenBox sites!"
)

number = st.slider("Pick a number", 0, 100)

