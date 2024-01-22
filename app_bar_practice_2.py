from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
#:import CustomOverFlowMenu __main__.CustomOverFlowMenu


MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MDTopAppBar"
        use_overflow: True
        overflow_cls: CustomOverFlowMenu()
        right_action_items:
            [
            ["home", lambda x: app.callback(x), "Home", "Home"],
            ["message-star", lambda x: app.callback(x), "Message star", "Message star"],
            ["message-question", lambda x: app.callback(x), "Message question", "Message question"],
            ["message-reply", lambda x: app.callback(x), "Message reply", "Message reply"],
            ]

    MDLabel:
        text: "Content"
        halign: "center"
'''


class CustomOverFlowMenu(MDDropdownMenu):
    # In this class you can set custom properties for the overflow menu.
    pass


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)


Test().run()
