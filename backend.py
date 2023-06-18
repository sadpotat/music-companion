""" Contains functions for main.py. """

import json
import requests
import base64
from bs4 import BeautifulSoup


def get_values(location):
    """ gets tokens """
    with open(location, "r") as file:
        value = file.read()
    return value


ACCESS_TOKEN = get_values("access_token.txt")
CLIENT_ID = get_values("client_id.txt")
CLIENT_SECRET = get_values("client_secret.txt")

# Replace YOUR_ACCESS_TOKEN with your actual access token
headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}


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


def get_song_data(query):
    """ This functions gets the queried song's information 
        from the Genius API, returns json_data dictionary.
        The query must be SONG_NAME and ARTIST_NAME"""

    # Searches for the song using the Genius API
    search_url = 'https://api.genius.com/search?q=' + query
    response = requests.get(search_url, headers=headers)

    # Gets the first song from the search results
    json_data = response.json()
    song_api_path = json_data['response']['hits'][0]['result']['api_path']

    # Uses the song API path to get the full song information
    song_url = 'https://api.genius.com' + song_api_path
    response = requests.get(song_url, headers=headers)
    json_data = response.json()
    return json_data


def get_lyrics_search(json_data):
    """ Scrapes lyrics from the song in json_data """
    song_lyrics_url = json_data['response']['song']['url']
    print(song_lyrics_url)
    response = requests.get(song_lyrics_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    lyrics_gen = soup.select(
        "div[class*=Lyrics__Container]")[0].strings
    lyrics = ""
    continue_loop = False
    for lyric in lyrics_gen:
        # skips the breaks inserted in place of <i> tags
        # I know this is an ugly workaround
        if "[" in lyric:
            lyric = "\n" + lyric
            if "]" in lyric:
                lyrics += lyric + "\n"
                # print(lyric)
                continue
            lyrics += lyric
            continue_loop = True
            # print(lyric)
            continue
        if "(" in lyric:
            if ")" in lyric:
                lyrics = lyrics + lyric + "\n"
                continue
            lyrics += lyric
            continue_loop = True
            continue
        if continue_loop:
            if "]" in lyric:
                lyrics += lyric + "\n"
                continue_loop = False
                # print(lyric)
                continue
            # print(lyric)
            if ")" in lyric:
                lyrics += lyric + "\n"
                continue_loop = False
                # print(lyric)
                continue
            # print(lyric)
            lyrics += lyric
            continue

        lyrics = lyrics + lyric + "\n"
    return lyrics

def get_details(json_data):
    return {
        "imageURL": json_data['response']['song']['header_image_thumbnail_url'],
        "title": json_data['response']['song']['title'],
        "artist": json_data['response']['song']['artist_names'],
        "album": json_data['response']['song']['album']['name'],
        "release_date": json_data['response']['song']['release_date_for_display'],
    }

def get_lyrics_audio(audio_stream):
    """ Calls Shazam API for Lyrics """
    return "These are some recognised lyrics\nMore lyrics\nMoore lyrics\
    \nMore lyrics\nMoore lyrics\nMore lyrics\nMoore lyrics"


if __name__ == "__main__":
    query = "you belong with me taylor swift"
    json_data = get_song_data(query)
    details = get_details(json_data)
    # for lyric in lyrics:
    #     print(lyric)
    print(details)
    # json_data['response']['song']['artist_names']
    # json_data['response']['song']['artist_names']
