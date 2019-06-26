import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout

class Menu_Screen(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.label_tittle = Label(text = "Puntuador\nScrabble",
												 color= (1,1,1,1),
												 font_size = 40,
												 halign = "center",
												 font_name= "Neothic.ttf",
												 size_hint = (0.2,0.1),
												 pos_hint = {"x":0.4,"y":0.7})
		self.add_widget(self.label_tittle)
		
		self.tog_but1 = ToggleButton(text = "2",
															size_hint = (0.1,0.05),
															pos_hint = {"x":0.35,"y":0.55},
															group = "player_number")
		self.tog_but2 = ToggleButton(text = "3",
															size_hint = (0.1,0.05),
															pos_hint = {"x":0.46,"y":0.55},
															group = "player_number")
		self.tog_but3 = ToggleButton(text = "4",
															size_hint = (0.1,0.05),
															pos_hint = {"x":0.57,"y":0.55},
															group = "player_number")	
		self.tog_but1.bind(on_press = self.setter_1)

		self.add_widget(self.tog_but1)
		self.add_widget(self.tog_but2)
		self.add_widget(self.tog_but3)
		
		# Label nombres
		
		self.label_instructions = Label(text = "Ingrese el nombre de los jugadores",
															 color= (1,1,1,1),
															 font_size = 21,
															 halign = "center",
															 font_name= "Neothic.ttf",
															 size_hint = (0.2,0.1),
															 pos_hint = {"x":0.4,"y":0.42})
		self.add_widget(self.label_instructions)
		
		# TextBox 1
		self.player1_textinput = TextInput(multiline = False,
																	size_hint = (1,0.2))
																	
		# TextBox 2
		self.player2_textinput = TextInput(multiline = False,
																	size_hint = (1,0.2))
							
		# TextBox 3
		self.player3_textinput = TextInput(multiline = False,
																	size_hint = (1,0.2))
																	
		# TextBox 4
		self.player4_textinput = TextInput(multiline = False,
																	size_hint = (1,0.2))
		
		self.stack_layout = StackLayout(orientation = "vertical",
															size_hint = (0.4,0.25),
															pos_hint = {"x":0.3,"y":0.2})
		self.add_widget(self.stack_layout)
	
		#add input widgets to the box layout
		
	def setter_1(self, _):
																	
		self.stack_layout.add_widget(self.player1_textinput)
		self.stack_layout.add_widget(self.player2_textinput)
			
	def setter_2(self, _):
		self.stack_layout.add_widget(self.player1_textinput)
		self.stack_layout.add_widget(self.player2_textinput)
		self.stack_layout.add_widget(self.player3_textinput)
	
	def setter_3(self, _):
		self.stack_layout.add_widget(self.player1_textinput)
		self.stack_layout.add_widget(self.player2_textinput)
		self.stack_layout.add_widget(self.player3_textinput)
		self.stack_layout.add_widget(self.player4_textinput)

class Score_App(App):
	def build(self):

		self.screen_manager = ScreenManager()
		
		self.menu_screen = Menu_Screen()
		screen = Screen(name='menu')
		screen.add_widget(self.menu_screen)
		self.screen_manager.add_widget(screen)
			
		return self.screen_manager


if __name__=='__main__':
	m_app =Score_App()
	m_app.run()
	
