import streamlit as st
import requests

st.title("Find Your Vibe")
st.subheader("Music Genre Recommendation")

mood = st.selectbox(
    "Mood",
    ["Happy", "Relaxed", "Sad", "Excited"]
)

activity = st.selectbox(
    "Activity",
    ["Studying", "Driving", "Exercising", "Walking"]
)

tempo = st.selectbox(
    "Tempo",
    ["Slow", "Medium", "Fast"]
)

if st.button("Recommend"):

    response = requests.post(
        "http://back:8000/recommend",
        json={
            "mood": mood,
            "activity": activity,
            "tempo": tempo
        }
    )

    result = response.json()

    st.success(f"Genre: {result['genre']}")

    st.write("Artists")
    for artist in result["artists"]:
        st.write("-", artist)

    st.write("Reason")
    st.write(result["reason"])