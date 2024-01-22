from kivy.lang.builder import Builder

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<CardItem>
    size_hint_y: None
    height: "86dp"
    padding: "4dp"
    radius: 12

    FitImage:
        source: "https://previews.123rf.com/images/moremar/moremar1907/moremar190700033/132121691-the-face-of-a-happy-girl-avatar-of-a-laughing-young-woman-portrait-vector-flat-illustration.jpg"
        radius: root.radius
        size_hint_x: None
        width: root.height

    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: "6dp"
        padding: "12dp", 0, 0, 0
        pos_hint: {"center_y": .5}

        MDLabel:
            text: "Title text"
            font_style: "H5"
            bold: True
            adaptive_height: True

        MDLabel:
            text: "Subtitle text"
            theme_text_color: "Hint"
            adaptive_height: True


MDScreen:

    MDSliverAppbar:
        background_color: "2d4a50"

        MDSliverAppbarHeader:

            MDRelativeLayout:

                FitImage:
                    source: "https://t4.ftcdn.net/jpg/05/45/42/81/360_F_545428173_uyYWJoR9n5uJFYIWfDa2C49AzIECcU20.jpg" #"bg.jpg"

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"
            adaptive_height: True
'''


class CardItem(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elevation = 1


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for x in range(10):
            self.root.ids.content.add_widget(CardItem())


Example().run()
