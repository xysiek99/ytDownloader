yt_download_link = '''
MDTextField:
    hint_text: "Download URL"
    pos_hint: {'center_x': 0.5, 'center_y': 0.45}
    size_hint: .8, None
    mode: "rectangle"
'''

yt_toolbar = '''
MDToolbar:
    title: "YouTube Downloader"
    pos_hint: {"top": 1}
    elevation: 10
'''

video_button = '''
MDRaisedButton:
    text: "Video"
    pos_hint: {'center_x': 0.42, 'center_y': 0.30}
'''

sound_button = '''
MDRectangleFlatButton:
    text: "Sound"
    pos_hint: {'center_x': 0.58, 'center_y': 0.30}
'''
