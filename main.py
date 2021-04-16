from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

from ytDownloaderLayout import *
from ytDownloader import downloadItem, getTitle

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

    def close(self, event):
        self.dialog.dismiss()

    def download_video(self, instance):
        try:
            download_string = self.link.text
            downloadItem(download_string, "video")
            message = getTitle(download_string)
        except AttributeError: 
            pass
        except:
            message = "Error occured during downloading file"

    def download_sound(self, instance):
        try:
            download_string = self.link.text
            downloadItem(download_string, "sound")
            message = getTitle(download_string)
        except AttributeError:
            pass
        except:
            message = "Error occured during downloading file"

YouTubeDownloaderApp().run()