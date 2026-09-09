import streamlit as st

st.title("🎈🎈🎈 Just baloons and not math")
st.write(
    "I'm really into colors, I hope you too! Guess which is my favorite?"
)

options = ["1+3", "9-5", "2^2"]

answer = st.radio(
    "Sharan, what do you think is NOT my favorite color?",
    key="colors",
    options=options,
)

submitted = st.button("Guess")
if submitted and answer in options:
    st.write("Riiiiight!")
