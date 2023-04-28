import streamlit as st
from backend import set_background, get_lyrics_search, get_lyrics_audio

st.set_page_config(page_title="Companion",
                   page_icon=":musical_note:", layout="centered")

st.markdown(
    """
    <style>
    .column {
        float: left;
        width: 50%;
        min-width: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

background = set_background("bg.jpg")
st.markdown(background, unsafe_allow_html=True)

if "lyrics" not in st.session_state:
    st.session_state.lyrics = ""
    st.session_state.height = None


def search_callback():
    st.session_state.lyrics = get_lyrics_search(user_search)
    count = st.session_state.lyrics.count("\n")
    st.session_state.height = count*30
    print("search_callback")


def audio_callback():
    st.session_state.lyrics = get_lyrics_audio("idk what to pass")
    count = count = st.session_state.lyrics.count("\n")
    st.session_state.height = count*30
    print("audio_callback")


with st.container():
    col1, col2 = st.columns([2, 1])

    with col1:
        user_search = st.text_input("**Enter Title and Artist**", placeholder="Song Title;Artist",
                                    help="Enter a song to view its lyrics, or press the mic icon for song recognition",
                                    on_change=search_callback, key="inputbox")

    with col2:
        user_audio = st.button(":studio_microphone:",
                               on_click=audio_callback, key="audio")

st.text_area("**Lyrics:**", st.session_state.lyrics,
             height=st.session_state.height)


print(st.session_state)
