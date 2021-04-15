import youtube_dl as yt

url = "https://www.youtube.com/watch?v=BOYdZ0GyQFQ&ab_channel=PearlJam"

# How to get information about the video
# As it is a dict use below instead of: vinfo.title
'''
vinfo = video.extract_info(url, download=False)
print(vinfo['title'])
print(vinfo['ext'])
print(vinfo['format']) 
'''

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
