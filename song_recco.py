import requests
from bs4 import BeautifulSoup
from re import findall
from random import sample

def search_vid(search):
    url = requests.get('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(url.text, "html.parser")
    try:
        first_div = soup.find("div", { "class" : "yt-lockup-content"})
    
        href= first_div.find('a', href=True)
        header = href.text
        video_link = "https://www.youtube.com"+href['href']
        return {"header" : header, "youtube_link" : video_link}

    except:
        pass
