import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
		

class Home_Screen(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.button1= Button(text="Puntuar",
											  pos_hint={"x":0.1,"y":0.2},
											  size_hint=(.2,.1))
		self.add_widget(self.button1)
		self.button1.bind(on_press=self.scorer)
		
		self.txin_player1 = TextInput(text="hola",
															multiline=False,
															pos_hint={"x":0.1,"y":0.4},
															size_hint=(.2,.1))
		self.add_widget(self.txin_player1)
		
		self.labl_score = Label(text="0",
												 color= (.1,.1,.1,.1),
												 pos_hint={"x":0.1,"y":0.4},
												 size_hint=(.2,.1))
		self.add_widget(self.txin_player1)
		
		
		
	def scorer(self, value):
			value_input = "hola"
			letters=[ ]
			letters=list(value_input)
			dic_letters= {" ":0,"a":1,"e":1,"o":1,"s":1,"i":1,"u":1,"n":1,"l":4,"r":4,"t":1,"c":2,"d":2,"g":2,"m":3,"b":3,"p":3,"f":4,"h":4,"v":4,"y":4,"j":6,"k":8,"ñ":8,"q":8,"w":8,"x":8,"z":10}
			par_score= [ ]
			for a in letters:
				letter_score = dic_letters[a]
				par_score.append(letter_score)
			self.psp1=sum(par_score)
			return print(self.psp1)
		
class test(App):
	def build(self):
		self.screen_manager = ScreenManager()
		
		self.home_screen = Home_Screen()
		screen = Screen(name="home")
		screen.add_widget(self.home_screen)
		self.screen_manager.add_widget(screen)
		
		return self.screen_manager
		
if __name__=='__main__':
	tapp=test()
	tapp.run()
