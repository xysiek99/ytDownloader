kv_layout = '''
Screen:
    BoxLayout:                    
        
'''

yt_download_link = '''
MDTextField:
    hint_text: "Download URL"
    helper_text: "Paste link to the video you want to download"
    helper_text_mode: "on_focus"
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