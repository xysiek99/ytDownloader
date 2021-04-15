import youtube_dl as yt

# USEFUL LINKS:
#
# https://stackoverflow.com/questions/49246598/youtube-dl-get-audio-link-with-python
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#configuration

def ignoreErrors():
    pass

def downloadItem(link, type):    
    if type == "video":
        options = {'outtmpl': '%(title)s.%(ext)s'}
    if type == "sound":
        options = {'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}
    
    item = yt.YoutubeDL(options)
    item.download([link])

def getTitle(link):
    material = yt.YoutubeDL().extract_info(url=link, download=False)
    return material['title']