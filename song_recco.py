from googleapiclient.discovery import build

api_key = #####

youtube = build('youtube', 'v3', developerKey=api_key)

def search_vid(search):
    try:
        req = youtube.search().list(part='snippet', q=search, type='video', maxResults=1)
        res = req.execute()
        res = res["items"][0]
        video_link = "https://www.youtube.com/watch?v=" + (res['id'])["videoId"]
        header = (res["snippet"])["title"]
        if "&amp;" in header:
            header = header.replace("&amp;", "&")
        if "&#39;" in header:
            header = header.replace("&#39;", "'")
        if "&quot;" in header:
            header = header.replace("&quot;", "'")
        return {"header" : header, "youtube_link" : video_link}
    except:
        pass

