from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton

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

    def show_message(self, message):
        ok_btn = MDRectangleFlatButton(text="OK")
        ok_btn.bind(on_press=self.close)

        self.dialog = MDDialog (
        title="INFO",
        text=message,
        size_hint=(.8, 1),
        buttons=[ok_btn]
        )
        self.dialog.open()

    def close(self, event):
        self.dialog.dismiss()

    def download_video(self, instance):
        download_string = self.link.text
        video_title = getTitle(download_string)
        success_message = f"{video_title} downloaded succesfully!"
        error_message = "Error occured during downloading file"

        try:
            downloadItem(download_string, "video")
            self.show_message(success_message)
        except AttributeError: 
            self.show_message(success_message)
        except:
            self.show_message(error_message)

    def download_sound(self, instance):
        download_string = self.link.text
        video_title = getTitle(download_string)
        success_message = f"{video_title} downloaded succesfully!"
        error_message = "Error occured during downloading file"

        try:
            downloadItem(download_string, "sound")
            self.show_message(success_message)
        except AttributeError: 
            self.show_message(success_message)
        except:
            self.show_message(error_message)

YouTubeDownloaderApp().run()

# https://www.youtube.com/watch?v=im9XuJJXylw&ab_channel=RetroTVCentral