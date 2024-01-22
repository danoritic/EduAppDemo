# from kivyMD import MDApp  !!!!!!!!

from kivymd.uix.textfield.textfield import MDTextField,MDTextFieldRect

from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from  kivy.uix.behaviors import TouchRippleBehavior,ButtonBehavior
from kivy.lang import Builder

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout


# custom module
from custom_behavior import HoverAndOtherBehavior,Elevated

class SignupMainLayout(FloatLayout):
    def do(*args):
        args[0].ids.sign_up_button.on_release=args[0].undo
        #print(args[0].ids.sign_up_button.on_release)
        print('crisk')
    def undo(*args):
        args[0].ids.sign_up_button.on_release=args[0].do
        print('uncrisk')

class MyScreenManager(ScreenManager):
    pass



class SmartButton(HoverAndOtherBehavior,Button):
    pass
Window.size=(300,(932/430)*300)
if __name__=="__main__":
    from kivy.app import App
    from kivymd.app import MDApp
    class SignUpPageApp(MDApp):
        def build(self):
            return SignupMainLayout()

    SignUpPageApp().run()


"""
border_image = BorderImage(
                source='tex.png',
                border=(10, 10, 10, 10),
                size=(b.width + 100, b.height + 100),
            )
"""
