from kivy.app import App
from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from  kivy.uix.behaviors import TouchRippleBehavior
from kivymd.uix.card.card import MDCard
from kivy.properties import Clock

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel


# custom module
from custom_behavior import HoverAndOtherBehavior
#Builder.load_file("SignUpPage.kv

class MyScreen(Screen):
    with open("C:\\Users\\USER\\Downloads\\AnimePahe_Shingeki_no_Kyojin_-_60_BD_720p_SCY.mp4","rb") as f:
        byter=f.read()
    #asyncprint(byter)
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    def do(*args):
        self.ids.player_widget.play=False if self.ids.player_widget.play else True
class VideoApp(MDApp):
    def build(self,):
        return MyScreen()


VideoApp().run()
