from youtube_api import YouTubeDataAPI

def getUrl(search_query):
    yt = YouTubeDataAPI("")  #Get api key from google cloud console

    video_id = yt.search(q=search_query)[0]["video_id"]

    url = f'https://youtu.be/{video_id}?feature=shared'
    return url