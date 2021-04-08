from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer

class TestLayout(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class TestApp(MDApp):
    def build(self):
        return TestLayout()

if __name__ == "__main__":
    TestApp().run()