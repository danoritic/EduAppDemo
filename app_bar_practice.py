from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:



    # Will always be at the bottom of the screen.
                MDBottomAppBar:
                    elevation:0

                    MDTopAppBar:
                        
                        elevation:0
                        title: "Title"
                        icon: "git"
                        type: "bottom"
                        anchor_title:"center"
                        use_overflow:True
                        right_action_items:
                            [
                            ["home", lambda x: app.callback(x), "Home"],
                            ["message-star", lambda x: app.callback(x), "Message star"],
                            ["message-question", lambda x: app.callback(x), "Message question"],
                            ["message-reply", lambda x: app.callback(x), "Message reply"],
                            ]
                        md_bg_bottom_color:0,1,1,1
                MDNavigationDrawer:
                    id:nav_drawer
                    
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def callback(self,i):
        print(i)


Test().run()
