from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

from ytDownloaderLayout import *

Window.size = (800,520)

'''
class TestLayout(MDScreen):
    def __init__(self, **kwargs):
        super(TestLayout, self).__init__(**kwargs)

        link = Builder.load_string(yt_download_link)
        toolbar = Builder.load_string(yt_toolbar)
        video_btn = Builder.load_string(video_button)
        sound_btn = Builder.load_string(sound_button)

        self.add_widget(link)
        self.add_widget(toolbar)
        self.add_widget(video_btn)
        self.add_widget(sound_btn)
'''

class TestApp(MDApp):
    def build(self):        
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        screen = MDScreen()

        link = Builder.load_string(yt_download_link)
        toolbar = Builder.load_string(yt_toolbar)
        video_btn = Builder.load_string(video_button)
        sound_btn = Builder.load_string(sound_button)

        sound_btn.bind(on_press=self.callback)

        screen.add_widget(link)
        screen.add_widget(toolbar)
        screen.add_widget(video_btn)
        screen.add_widget(sound_btn)

        return screen

    def callback(self, instance):
        print("Hello!")

TestApp().run()