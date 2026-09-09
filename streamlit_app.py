import streamlit as st

st.title("🎈🎈🎈 Just baloons and no math")
st.write(
    "I'm really into colors, I hope you too! Sharan, can you guess what is my favorite color?"
)

options = ["1+3", "9-5", "2^2"]

answer = st.radio(
    "",
    options=options,
)

submitted = st.button("Guess")
if submitted and answer in options:
    st.write("Riiiiight!")
    st.balloons()
