import streamlit as st

st.title("🎈🎈🎈 Just baloons and no math")
st.write(
    "I'm into  typographically pretty text rendering, I hope you too!"
)

a = r"$\sum_{k=0}^{n-1} ar^k$"
b = "different font size of this question compared to the text before"
c = "double spaces between words (can you find any?)"
d = r"$a^2$"
e = "none of the above"

answer = st.radio(
    "Sharan, to check your sense of typographic beauty, guess what I find disturbing:",
    [a,b,d,c,e],
)

submitted = st.button("Guess")
if submitted:
    if answer in [b,c]:
        st.write("Riiiiight!")
        st.balloons()
    else:
        st.write("Sigh...")
