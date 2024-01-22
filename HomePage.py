# from kivy.app import App
from kivymd.app import MDApp

# from kivymd.tools.hotreload.app import MDApp

from kivy.loader import Loader
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.behaviors import TouchRippleBehavior
from kivymd.uix.card.card import MDCard
from kivy.properties import Clock

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel


# custom module
from custom_behavior import HoverAndOtherBehavior
from Sign_up_page import *

# Builder.load_file("SignUpPage.kv

for i in dir(MDCard):
    if "__" not in i and "shadow" in i:
        print(i)


class CustumListItem:
    pass


class ModalTab(ModalView):
    string = """
<ModalTab>:
    #padding:[dp(14),dp(14),0,dp(14)]
    pos_hint:{"center_x":.5}
    #id:ModalTab
    size_hint:.7,.7
    deller:"deller"
    FloatLayout:
        id:free
        size_hint:1,1
        canvas.before:
            Color:
                rgba:1.00, 0.95, 0.80,1
            RoundedRectangle:
                pos:self.pos
                size: self.size

        ScrollView:
            pos_hint:{"center_x":.5,"center_y":.5}
            pos:free.pos
            size_hint:1,.9
            BoxLayout:
                spacing:5
                padding:[dp(14),dp(14),0,dp(14)]
                pos_hint:{"center_x":.5}
                size_hint:1,None
                height:self.minimum_height
                orientation:"vertical"
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                SmartButton:
                    size_hint:None,None
                    size:dp(200),dp(50)
                    background_color:0,0,0,0
                    canvas.before:
                        Color:
                            rgba:0,.5,0,1
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[5,]
                
                            """
    Builder.load_string(string)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("don do")
        # Builder.load_string(self.string)


class HomePageMainframe(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def callback2(self, *args):
        print(args)
        self.ids.bottom_box.clear_widgets()
        self.ids.bottom_box_label.text = "Nuggets"
        self.ids.bottom_box.add_widget(BottomBoxNugget())

    def callback(self, *args):
        print(args)
        self.ids.bottom_box.clear_widgets()
        self.ids.bottom_box_label.text = "Tutorial Videos"
        self.ids.bottom_box.add_widget(BottomBoxTutorialVideo())

        # opacity=0


class BottomBoxTutorialVideo(BoxLayout):
    pass


class BottomBoxNugget(StackLayout):
    pass


class MyScroll(ScrollView):
    pass

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.scroll_timeout = 55
        # self.scroll_distance=20
        super().on_touch_up(touch)


class MyCarousel(Carousel):
    pass


class HomePageApp(MDApp):
    # DEBUG=1
    def build(
        self,
    ):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"  # "Dark"
        self.theme_cls.primary_palette = "Orange"
        print("*" * 10)
        for i in dir(Loader.image):
            if "__" not in i:
                print(i)
        Loader.loading_image = "loading.gif"
        Loader.loading_image.keep_data = False
        # Loader.loading_image.size=[50,50]
        print(Loader.loading_image.keep_data, Loader.loading_image.size)  #
        return HomePageMainframe()


class CourseCard(RelativeLayout):
    modal_view = ModalTab(size_hint=(0.77, 0.7))

    def display_view(self, *args):
        print(self.modal_view.deller)
        self.modal_view.open()
        self._open = True

    def close_view(self, *args):
        self.modal_view.dismiss()
        self._open = False


if __name__ == "__main__":
    HomePageApp().run()
