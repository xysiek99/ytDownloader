from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window

from ytDownloaderLayout import *

Window.size = (800,520)

class TestLayout(Screen):
    def __init__(self, **kwargs):
        super(TestLayout, self).__init__(**kwargs)

        self.link = Builder.load_string(yt_download_link)
        self.toolbar = Builder.load_string(yt_toolbar)

        self.add_widget(self.link)
        self.add_widget(self.toolbar)

class TestApp(MDApp):
    def build(self):        
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        return TestLayout()

if __name__ == "__main__":
    TestApp().run()