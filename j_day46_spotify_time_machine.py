import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

era = input("Which date would you like to travel to? Type this data in the format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{era}")
music_list = response.text

soup = BeautifulSoup(music_list, "html.parser")

songs = soup.select(".o-chart-results-list__item .c-title")

song_list = [song.getText().strip() for song in songs]
print(song_list)

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]
year = era.split("-")[0]

song_uris = []

for song in song_list:
    track = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = track["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

new_playlist = sp.user_playlist_create(user_id, f"{era} - Billboard Top 100", public=False,
                                       description="Billboards top 100 from your chosen era!")

print(new_playlist["id"])
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)