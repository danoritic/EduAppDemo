

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title: "Edited Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    #md_bg_color: "#e7e4c0"
                    md_bg_color:0,1,1,0
                    specific_text_color: "#4a4939"
                    left_action_items:[['menu', lambda x: nav_drawer.set_state("open")]]
                    #radius:[10,]
        MDNavigationDrawer:
            id: nav_drawer
            radius:(0, 16, 16, 0) # [10,] #
            md_bg_color:0,1,1,.5
            canvas.after:
                Color:
                    rgba:0,1,1,.0
                RoundedRectangle:
                    pos:self.pos #[i*.5 for i in self.pos]
                    size:self.size  #[i*.1 for i in self.size]
                    radius:nav_drawer.radius
            ContentNavigationDrawer:
                
                    
'''
class ContentNavigationDrawer(MDBoxLayout):
    pass
class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

Example().run()

