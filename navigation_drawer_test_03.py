from kivy.lang.builder import Builder

from kivymd.app import MDApp

kv = '''
<MagicButton@MagicBehavior+MDIconButton>


<MySwiper@MDSwiperItem>

    RelativeLayout:

        FitImage:
            source: "guitar.jpg"
            radius: [20,]

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            MagicButton:
                id: icon
                icon: "weather-sunny"
                user_font_size: "56sp"
                opposite_colors: False

            MDLabel:
                text: "MDLabel"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}
                opposite_colors: True


MDScreen:

    MDTopAppBar:
        id: toolbar
        title: "MDTopAppBar"
        right_action_items: [["dots-vertical", lambda x: app.callback()]]
        elevation: 4
        pos_hint: {"top": 1}

    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(40)
        y: root.height - self.height - toolbar.height - dp(20)
        on_swipe: self.get_current_item().ids.icon.shake()

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def callback(self):
        print("scobidoo")


Main().run()
