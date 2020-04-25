from random import sample
from genre_finder import genre_finder as genre_finder
from song_recco import search_vid as search_vid
from spotify_link import spotify_link as spotify_link
from genre_finder import recommend_songs as recommend_songs
import time


def main_recco(song):
    res = []
    genres = genre_finder(song)
    for genre in genres:
        for x in recommend_songs(genre, song):
            res.append(" ".join(x.values()))

    final_res = res
    links_ = []

    for result in final_res:
        full_link = search_vid(result)

        if full_link:
            try:
                full_link.update({"spotify_link" : spotify_link(result)})

            except:
                pass

            links_.append(full_link)

    return links_

