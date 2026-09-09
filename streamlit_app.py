import streamlit as st

st.title("🎈🎈🎈 Just baloons and not math")
st.write(
    "I'm really into colors, I hope you too! Guess which is my favorite?"
)

options = ["1+3", "9-5", "2^2"]
st.radio(
    "Sharan, what do you think is NOT my favorite color?",
    key="colors",
    options=options,
)
answer = st.select_box("Guess", options)
if answer == "9-5":
    st.write("Riiiiight!")
else:
    st.write("Riiiiight!")