import youtube_dl as yt

yt_ops = {'outtmpl': '%(id)s.%(ext)s'}
video = yt.YoutubeDL(yt_ops)
url = "https://www.youtube.com/watch?v=7Kofui217Vk&ab_channel=MatthewOlson"

vinfo = video.extract_info(url, download=False)
print(vinfo)

#video.download(["https://www.youtube.com/watch?v=7Kofui217Vk&ab_channel=MatthewOlson"])