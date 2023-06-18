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

# sets background image
background = be.set_background("bg.jpg")
st.markdown(background, unsafe_allow_html=True)

# defining the state variables we'll need
if "lyrics" not in st.session_state:
    st.session_state.lyrics = ""
    st.session_state.height = None
    st.session_state.details = None


# callback function for search
def search_callback():
    json_data = be.get_song_data(st.session_state.inputbox)
    st.session_state.details = be.get_details(json_data)
    st.session_state.lyrics = be.get_lyrics_search(json_data)
    print("search_callback")


# callback function for audio button
def audio_callback():
    st.session_state.lyrics = be.get_lyrics_audio("idk what to pass")
    print("audio_callback")


# placing searchbox and audio button
with st.container():
    input_col, button_col = st.columns([10, 1])

    with input_col:
        user_search = st.text_input("**Enter Title and Artist**", placeholder="Song_title Artist_name",
                                    help="Enter a song to view its lyrics, or press the mic icon for song recognition",
                                    on_change=search_callback, key="inputbox")

    with button_col:
        st.write("")
        user_audio = st.button(":studio_microphone:",
                               on_click=audio_callback, key="audio")

# song details will only appear after a search
if st.session_state.details:
    # CSS for st.image
    st.markdown(
    """
    <style>
    div[data-testid="column"]:nth-of-type(2) 
    {
    display: block;
    margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True)
    
    # CSS for song details
    st.markdown(
    """
    <style>
    div[data-testid="column"]:nth-of-type(3) 
    {
    background-color: rgba(66, 198, 237, 0.7);
    border-radius: 3rem;
    text-align: left;
    padding-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True)

    # CSS for song details text
    st.markdown(
    """
    <style>
    div[data-testid="stText"]:nth-of-type(1) 
    {
    padding-left: 30px;
    font-family: Arial;
    font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True)

    with st.container():
        pad1, album_art, song_info, pad2 = st.columns([1, 3, 6, 1], )
        
        with album_art:
            # st.markdown(f"![Album Art]({st.session_state.details['imageURL']})" +"{width=200}")
            st.image(st.session_state.details["imageURL"])
            
        with song_info:
            st.text(f"Title: {st.session_state.details['title']}")
            st.text(f"Album: {st.session_state.details['album']}")
            st.text(f"Artist: {st.session_state.details['artist']}")
            st.text(f"Release Date: {st.session_state.details['release_date']}")

# display lyrics
st.text_area("**Lyrics:**", st.session_state.lyrics,
             height=500)


print(st.session_state)
