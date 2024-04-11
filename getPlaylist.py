import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from getYoutubeUrl import getUrl
from download import download

def getPlaylist(spotify_url, path):
    playlist_id = spotify_url.split("/").pop().split("?")[0]
    #Get client_id and client_secret from spotify developers dashboard
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="", client_secret=""))
    results = spotify.playlist(playlist_id=playlist_id)
    folder_name = results["name"]
    for track in results["tracks"]["items"]:
        search_query = track["track"]["name"] + " "
        for artist in track["track"]["artists"]:
            search_query += artist["name"] + ", "
        search_query = search_query[:-2]
        youtube_url = getUrl(search_query)
        download(url=youtube_url, path=path+"/"+folder_name)


