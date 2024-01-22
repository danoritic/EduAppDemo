from kivy.core.window import Window
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from  kivy.uix.behaviors import TouchRippleBehavior
from kivymd.uix.textfield.textfield import MDTextField,MDTextFieldRect
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
    RectangularElevationBehavior,
)

class Elevated( # TextInput
    #RectangularRippleBehavior,
    
    CommonElevationBehavior,
    BackgroundColorBehavior,
    #MDTextFieldRect,
    
    RelativeLayout
    
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.md_bg_color = "red"



class HoverAndOtherBehavior(TouchRippleBehavior,object):
    """Hover behavior.

    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget 
    """

    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverAndOtherBehavior, self).__init__(**kwargs)


    def on_mouse_pos(self, *args):
        pos = args[1]
        inside = self.collide_point(*pos)
        if self.hovered == inside:
            #We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        self.color=[i-.2 for i in self.color[:3]]+[1]

    def on_leave(self):
        self.color=[i+.2 for i in self.color[:3]]+[1]

    def on_touch_down(self, touch):
            # print(touch)
            collide_point = self.collide_point(touch.x, touch.y)
            
            # collide_point = self.collide_point(touch[0], touch[1])
            if collide_point:
                touch.grab(self)
                self.ripple_duration_in = .7
                #self.ripple_scale = 0.1
                self.ripple_show(touch)
                self.dispatch('on_press')
                return True
            return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_duration_out = 0.7
            self.ripple_fade()
            self.dispatch('on_release')
            return True
        return False
