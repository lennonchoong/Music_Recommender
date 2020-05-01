from selenium import webdriver
from random import sample
import os

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#op.add_argument('headless')
op.add_argument('--headless')
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--no-sandbox")
classes = ['div.Z0LcW',
           'div.TZNJBf',
           '#rso > div:nth-child(1) > div.kp-blk.EyBRub.c14z5c.Wnoohf.OJXvsb > div.xpdopen > div.ifM9O > div > div.SALvLe.farUxc.mJ2Mod > div > div:nth-child(4) > div > div > span.LrzXr.kno-fv > a',
           'LrzXr.kno-fv',
           'LrzXr.kno-fv']


def genre_finder(songs):
    song_list_sample = []
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
    #browser = webdriver.Chrome(options=op)

    browser.get("https://www.google.com/search?q=genre+{}".format(songs.replace(" ", "+")))

    for i in classes:
        try:
            genre = browser.find_element_by_css_selector(i)
            song_list_sample.append(genre.text)
        except:
            pass
    browser.quit()
    return [x for x in song_list_sample if x] ##### result #####

def recommend_songs(genre, input_song):
    recommended_list = []
    urls = ["https://www.google.com/search?q=songs+like+{}".format(input_song.replace(" ", "+")), "https://www.google.com/search?q={}+songs".format(genre.replace(" ", "+"))]
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
    #browser = webdriver.Chrome(options=op)
    
    if '&' in genre: 
        genre = genre.replace('&', '%26')

    for url in urls:
        browser.get(url)
        i = 0
        songs = zip(browser.find_elements_by_css_selector("div.title"), browser.find_elements_by_css_selector("div.uDMnUc"))
        for artist, song in songs:
            if input_song not in song.text and i < 12:
                recommended_list.append({"song": artist.text, "artist": (song.text).split(" ·")[0]})
                i += 1
    recommended_list = sample(recommended_list, 8)
    browser.quit()
    return recommended_list

