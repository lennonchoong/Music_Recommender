import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from re import findall

cid = "2f03e5a432d94dbdbde91a8b738096e6"
secret = "419f4a447f4649c6a1c301eb123db602"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def spotify_link(q):
    output = sp.search(q, 1, 0, "track", "US")
    result = findall("'(https://open.spotify.com/track/[A-z0-9]+)'", str(output))

    return result[0]


