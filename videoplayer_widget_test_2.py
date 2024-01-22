from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


class MainApp(MDApp):
	title = "Simple Video"
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
        
        # Create videoPlayer Instance
		player = VideoPlayer(source = "C:/Users/USER/Downloads/How To Block An Application From Accessing The Internet In Windows 11_10 [Tutorial].mp4")
	
		# Assign VideoPlayer State
		player.state = 'play'

		# Set options
		player.options = {'eos': 'loop'}

		# Allow stretch
		player.allow_stretch = True

		# Return player
		return player


MainApp().run()
