import youtube_dl as yt

video_options = {'outtmpl': '%(id)s.%(ext)s'}
sound_options = {'format': 'bestaudio'}

video = yt.YoutubeDL(video_options)
sound = yt.YoutubeDL(sound_options)

url = "https://www.youtube.com/watch?v=ua7TBlFbBjg&ab_channel=Franck"

vinfo = video.extract_info(url, download=False)

# How to get information about the video
# As it is a dict use below instead of: vinfo.title
'''
print(vinfo)
print(vinfo['title']) 
'''

video.download([url])
sound.download([url])

# USEFUL LINKS:
#
# https://stackoverflow.com/questions/49246598/youtube-dl-get-audio-link-with-python
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl