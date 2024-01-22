# from kivyMD import MDApp  !!!!!!!!
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.scrollview import ScrollView

from kivy.uix.textinput import TextInput
from kivymd.uix.textfield.textfield import MDTextField, MDTextFieldRect


from kivy.uix.button import Button
from kivy.uix.behaviors import TouchRippleBehavior
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
    RectangularElevationBehavior,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget


def do(*args):
    pass


"""
<ElevatedTextInput@Elevated>:
    size_hint:.9,None
    height:35
    elevation: 1.5
    shadow_offset: -1, 3
    shadow_softness: 5
    radius:[5]
    md_bg_color:1,1,1,1
    MDTextField:
        pos_hint:{"y":0}
        #mode:"fill"
        mode:"line"
        
        #text_color:1,0,0,1
        hint_text:'Enter your password'
        hint_text_font_size:"10dp"
        id:password_text_box
        #hint_text_color:0,0,0,1
        background_color:1,1,1,0
        #foreground_color:0,0,0,.5
        radius:[5]
        #valign:"center"
        #halign:"center"
        cursor_color:0,0,0,1
        
        
        font_size:"15dp"
        fill_color_normal:1,1,1,1
        fill_color_focus:1,1,1,1

        #hint_text_color_normal:0.24, 0.75, 0.24,1
        hint_text_color_focus:0.24, 0.75, 0.24,1
        text_color_normal:0.24, 0.75, 0.24,1
        text_color_focus:0.24, 0.75, 0.24,1
        

        color:0.24, 0.75, 0.24,1
        line_color_focus:0.24, 0.75, 0.24,1
        #set_active_underline_color:0.24, 0.75, 0.24,1

"""


# custom module
from custom_behavior import HoverAndOtherBehavior
from Sign_up_page import *

# Builder.load_file("SignUpPage.kv")
"""
    FloatLayout:
        id:image_handler
        size_hint:None,None
        size:0,0
        
5        FloatLayout:
            size_hint_y:None
            height:50
            padding:"50dp"
            Image:
                id:imaging
                source:"C:/code/serious_work/ios app for mr david/ElitePage_kivy/resource/rhs 2.png"
                #pos:self.width,root.width#root.width/2-self.width/2,(root.height/2)-20
                pos_hint:{"center_x":.5,"center_y":.3}
                height:1

                                #Button:
                #text:"why"
                #size_hint:None,None
                #size:50,90
                #pos_hint:{"center_x":.5}

"""


class Frame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = RelativeLayout()
        self.no_of_children = 0

    def add_widget(self, *args):
        super().add_widget(*args)
        self.layout.add_widget(*args)

    def on_pos(self, *args):
        self.layout.pos = args[1]

    def on_size(self, *args):
        self.layout.size = args[1]


class AuthMainLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

    def sign_in(self):
        pass
        # username=username_text_box.text

    def do(self, *args):
        print(self.ids.imaging.pos, self.ids.imaging.size)
        # print(args)
        # print(1234)


def do(*args):
    print(1)


class MyScroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dodo = 1
        self.do_scroll = False

    def do(self, *args):
        print(1)

    def on_touch_down(self, *args):
        # args[0].grab_current=FloatLayout()
        super().on_touch_down(*args)
        # print(args)
        self.args = args
        return None  # self.on_touch_move)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.current="login_page"


class LoginPageApp(MDApp):
    pass
    """
    def build(self):
        Builder.load_file("LoginPage.kv")
        canvas.before:
                
                Color:
                    rgba:0,0,0,.2
                RoundedRectangle:
                    size:[self.size[0]+2,self.size[1]]
                    pos:[self.pos[0]-1,self.pos[1]-3]
                    radius:[5]
                Color:
                    rgba:1,1,1,1
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[5]
                
                Color:
                    rgba:self.foreground_color
    """


class RectangularElevationButton(
    RectangularRippleBehavior,
    CommonElevationBehavior,
    ButtonBehavior,
    BackgroundColorBehavior,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = "red"


class Elevated(  # TextInput
    # RectangularRippleBehavior,
    # CommonElevationBehavior,
    BackgroundColorBehavior,
    RectangularElevationBehavior,
    # MDTextFieldRect,
    BoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.md_bg_color = "red"


class SmartButton(HoverAndOtherBehavior, Button):
    pass


Window.size = (300, (932 / 430) * 300)
print((932 / 430) * 300)
# Window.size=(300,500)

if __name__ == "__main__":
    LoginPageApp().run()


"""


<GrandMaster@ScrollView>:
    BoxLayout:
        size_hint_y:1
        height:self.minimum_height
        orientation:"vertical"
        id:scroll_box
        SignupMainLayout:
        AuthMainLayout:










border_image = BorderImage(
                source='tex.png',
                border=(10, 10, 10, 10),
                size=(b.width + 100, b.height + 100),
            )

MDTextField:
                mode:"rectangle"
                #text_color:1,0,0,1
                hint_text:'Enter your password'
                id:password_text_box
                #hint_text_color:0,0,0,1
                background_color:1,1,1,0
                #foreground_color:0,0,0,.5
                #valign:"center"
                #halign:"center"
                cursor_color:0,0,0,1
                
                font_size:"15dp"

"""
