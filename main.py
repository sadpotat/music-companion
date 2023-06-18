import streamlit as st
import backend as be

st.set_page_config(page_title="Companion",
                   page_icon=":musical_note:", layout="centered")

# st.markdown(
#     """
#     <style>
#     .column {
#         float: left;
#         width: 50%;
#         min-width: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

background = be.set_background("bg.jpg")
st.markdown(background, unsafe_allow_html=True)

if "lyrics" not in st.session_state:
    st.session_state.lyrics = ""
    st.session_state.height = None
    st.session_state.details = None


def search_callback():
    json_data = be.get_song_data(st.session_state.inputbox)
    st.session_state.details = be.get_details(json_data)
    st.session_state.lyrics = be.get_lyrics_search(json_data)
    print("search_callback")


def audio_callback():
    st.session_state.lyrics = be.get_lyrics_audio("idk what to pass")
    print("audio_callback")


with st.container():
    col1, col2 = st.columns([10, 1])

    with col1:
        user_search = st.text_input("**Enter Title and Artist**", placeholder="Song_title Artist_name",
                                    help="Enter a song to view its lyrics, or press the mic icon for song recognition",
                                    on_change=search_callback, key="inputbox")

    with col2:
        st.write("")
        user_audio = st.button(":studio_microphone:",
                               on_click=audio_callback, key="audio")

if st.session_state.details:
    st.text_area("Song Details", st.session_state.details,
                height=100)

st.text_area("**Lyrics:**", st.session_state.lyrics,
             height=500)


print(st.session_state)
