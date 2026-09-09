import streamlit as st
import pandas as pd
import numpy as np

languages = ['Basque', 'Kannada', 'Mapudungun', 'Passamaquoddy', 'Swahili', 'Warlpiri', 'penguin language']
continents = ['Europe', 'Asia', 'South America', 'North America', 'Africa', 'Australia', 'Antarctica']
speakers = [1_000_000, 50_000_000, 100_000, 500, 10_000_000, 2500, 15_000_000]
speakers_0 = [1_000_000, 50_000_000, 100_000, 500, 10_000_000, 2500, 15_000_000, 0, 1, 10]

st.title("Let's educate Sharan 🎈🎈🎈")
st.write(
    "Sharan, do you think you know the answer to this?!"
)

tab1, tab2 = st.tabs(["Language", "Families"])

with tab1:

    answer = st.radio(
        "Which language family does Passamaquoddy belong to?",
        ['Dravidian', 'Eskimo-Aleut', 'Indo-European', 'Semitic', 'none of the above'],
        index=None,
    )

    submitted = st.button("Guess")
    if submitted:
        if answer == 'none of the above':
            st.success("Riiiiight, it belongs to the Algonquian family!")
            st.balloons()
        elif answer == None:
            st.warning("Please select an option first.")
        elif answer == 'Eskimo-Aleut':
            st.error("Nice try, but...")
        else:
            st.error("Really?!")

    col1, col2 = st.columns(2)

    with col1:
        sboxanswer = st.selectbox(
            'Where is Passamaquoddy spoken?',
            options=continents,
            index=None,
        )
        if sboxanswer == None:
            pass
        elif sboxanswer == 'North America':
            st.success('Correct!')
        else:
            st.error('Nope.')

    with col2:
        slider_ans = st.select_slider(
            'By approximately how many speakers is it spoken?',
            np.sort(speakers_0),
        )
        if slider_ans == 0:
            pass
        elif slider_ans == 500:
            st.success("That's right!")
        else:
            st.error('Nope.')

with tab2:

    df = pd.DataFrame({
        'languages': languages,
        'continents': continents,
        'number of speakers': speakers,
    })

    st.dataframe(df)