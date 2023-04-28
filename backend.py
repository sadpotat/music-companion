""" Contains functions for main.py. """

import base64


def get_base64(bin_file):
    """ Converts an image to a base64 string. """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    """ Sets the background for the app. """
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    return page_bg_img


def get_lyrics_search(user_input):
    """ Calls Genius API for Lyrics """
    return "These are some lyrics\nMore lyrics\nMoore lyrics"


def get_lyrics_audio(audio_stream):
    """ Calls Shazam API for Lyrics """
    return "These are some recognised lyrics\nMore lyrics\nMoore lyrics\
    \nMore lyrics\nMoore lyrics\nMore lyrics\nMoore lyrics"
