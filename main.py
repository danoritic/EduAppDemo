# from kivyMD import MDApp  !!!!!!!!
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from  kivy.uix.behaviors import TouchRippleBehavior

from kivy.uix.anchorlayout import AnchorLayout

# custom module
from custom_behavior import HoverAndOtherBehavior
from Sign_up_page import *
#Builder.load_file("SignUpPage.kv")

class AuthMainLayout(AnchorLayout):
    def sign_in(self):
        username=username_text_box.text

class MyScreenManager(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.current="login_page"
class MainApp(App):
    pass


class SmartButton(HoverAndOtherBehavior,Button):
    pass

Window.size=(300,500)
if __name__=="__main__":
    MainApp().run()


"""
border_image = BorderImage(
                source='tex.png',
                border=(10, 10, 10, 10),
                size=(b.width + 100, b.height + 100),
            )
"""
