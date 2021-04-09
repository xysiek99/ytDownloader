from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.core.window import Window

Window.size = (800,520)

class TestLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class TestApp(MDApp):
    def build(self):        
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"

        return TestLayout()

if __name__ == "__main__":
    TestApp().run()