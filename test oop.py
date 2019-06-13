from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.first_layout = BoxLayout()
        self.first_layout.orientation = "vertical"
        self.first_layout.size_hint = (0.4, 1)
        self.first_layout.pos_hint = {"x":0.3,"y":0.1}
        self.add_widget(self.first_layout)

        # Label con el nombre del Jugador
        self.labl_player = Label(text="Jugador",
                                 color= (1,0,0,1))
        self.first_layout.add_widget(self.labl_player)

        # Label con la puntuacion actual
        self.labl_score = Label(text="Puntuacion",
                                font_size = 20,
                                color=(0, 1, 0, 1))
        self.first_layout.add_widget(self.labl_score)

        # Caja de texto para introducir palabras
        self.txinp1 = TextInput(size_hint=(1,0.2),
                                multiline=False)
        self.first_layout.add_widget(self.txinp1)

        self.button_score = Button(text="Calcular")
        self.first_layout.add_widget(self.button_score)




        # for the navigation buttons at the end of the screen
        self.nav_layout = BoxLayout()
        self.nav_layout.orientation = "horizontal"
        self.nav_layout.size_hint = (1, 0.08)
        self.add_widget(self.nav_layout)

        self.labl_blank = Label()
        self.nav_layout.add_widget(self.labl_blank)

        self.labl_blank2 = Label()
        self.nav_layout.add_widget(self.labl_blank2)

        self.bot4 = Button(text="Siguiente",
                           shorten=True)
        self.nav_layout.add_widget(self.bot4)


class TestApp(App):
    def build(self):
        # screen manager para cambiar screen
        self.screen_manager = ScreenManager()

        # home screen config
        self.home_screen = HomeScreen()
        screen = Screen(name="home")
        screen.add_widget(self.home_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    main_app = TestApp()
    main_app.run()
