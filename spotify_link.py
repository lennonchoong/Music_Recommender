import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from re import findall

cid = ####
secret = ####

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def spotify_link(q):
    output = sp.search(q, 1, 0, "track", "US")
    result = findall("'(https://open.spotify.com/track/[A-z0-9]+)'", str(output))

    return result[0]


