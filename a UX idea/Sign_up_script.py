# from kivyMD import MDApp  !!!!!!!!
from kivy.app import App

from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from  kivy.uix.behaviors import TouchRippleBehavior
from kivy.lang import Builder

from kivy.uix.anchorlayout import AnchorLayout

# custom module
from custom_behavior import HoverAndOtherBehavior

class SignupMainLayout(AnchorLayout):
    pass

class MyScreenManager(ScreenManager):
    pass
class SignUpPageApp(App):
    pass


class SmartButton(HoverAndOtherBehavior,Button):
    pass

Window.size=(300,500)
if __name__=="__main__":
    SignUpPageApp().run()


"""
border_image = BorderImage(
                source='tex.png',
                border=(10, 10, 10, 10),
                size=(b.width + 100, b.height + 100),
            )
"""
