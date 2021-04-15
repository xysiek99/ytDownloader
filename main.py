from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

from ytDownloaderLayout import *
from ytDownloader import downloadItem

Window.size = (800,520)

class YouTubeDownloaderApp(MDApp):
    def build(self):        
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        screen = MDScreen()

        self.link = Builder.load_string(yt_download_link)
        toolbar = Builder.load_string(yt_toolbar)
        video_btn = Builder.load_string(video_button)
        sound_btn = Builder.load_string(sound_button)

        video_btn.bind(on_press=self.download_video)
        sound_btn.bind(on_press=self.download_sound)

        screen.add_widget(self.link)
        screen.add_widget(toolbar)
        screen.add_widget(video_btn)
        screen.add_widget(sound_btn)

        return screen

    def download_video(self, instance):
        download_string = self.link.text
        downloadItem(download_string, "video")
        print(download_string)

        #dialog = MDDialog(title="Info", text="downloaded succesfully!")
        #dialog.open()    

    def download_sound(self, instance):
        download_string = self.link.text
        downloadItem(download_string, "sound")
        print(download_string)    

    def message_box(self, message_text):
        pass

YouTubeDownloaderApp().run()