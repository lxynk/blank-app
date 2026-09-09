import streamlit as st

st.title("🎈🎈🎈 Just baloons and no math")
st.write(
    "I'm into  typographically pretty text rendering, I hope you too!"
)

a = st.latex(r"\sum_{k=0}^{n-1} ar^k")
b = "different font size of this question compared to the text before"
c = "double spaces between words (can you find any?)"
d = st.latex(r"a^2")
e = "none of the above"

answer = st.radio(
    "Sharan, to check your sense of typographic beauty, guess what I find disturbing:",
    options=[
        st.latex(r"\sum_{k=0}^{n-1} ar^k"),
        "different font size of this question compared to the text before",
        "double spaces between words (can you find any?)",
        st.latex(r"a^2"),
        "none of the above",
        ],
)

submitted = st.button("Guess")
if submitted and answer in [b,c]:
    st.write("Riiiiight!")
    st.balloons()
elif submitted and answer not in [b,c]:
    st.write("Sigh...")