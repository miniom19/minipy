from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition


class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.first_layout = BoxLayout()
        self.first_layout.orientation = "vertical"
        self.first_layout.size_hint = (0.4, 1)
        self.first_layout.pos_hint = {"x": 0.3, "y": 0.1}
        self.add_widget(self.first_layout)

        # Label con el nombre del Jugador
        self.labl_player = Label(text="Jugador",
                                 color=(1, 0, 0, 1))
        self.first_layout.add_widget(self.labl_player)

        # Caja de texto para introducir palabras
        self.txinp1 = TextInput(size_hint=(1, 0.2),
                                multiline=False)
        self.txinp1.input_type= "text"
        self.first_layout.add_widget(self.txinp1)

        # Label con la puntuacion actual
        self.labl_score = Label(text="Puntuacion",
                                font_size=20,
                                color=(0, 1, 0, 1))
        self.first_layout.add_widget(self.labl_score)

        # boton para calcular puntuacion
        self.button_score = Button(text="Calcular",
                                   size_hint=(1, 0.3))
        self.first_layout.add_widget(self.button_score)
        self.button_score.bind(on_press= self.score_maker)

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
        self.bot4.bind(on_press= self.swap_game)

    def swap_game(self, _):
        main_app.screen_manager.current="game"

    def score_maker(self,_):
        value_input = str(self.txinp1.text)
        letters = list(value_input)
        dic_letters = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0," ": 0, "a": 1, "e": 1, "o": 1, "s": 1, "i": 1, "u": 1, "n": 1, "l": 4, "r": 4, "t": 1, "c": 2,"d": 2, "g": 2, "m": 3, "b": 3, "p": 3, "f": 4, "h": 4, "v": 4, "y": 4, "j": 6, "k": 8, "ñ": 8,"q": 8, "w": 8, "x": 8, "z": 10}
        par_score = []
        for a in letters:
            letter_score = dic_letters[a]
            par_score.append(letter_score)
        psp1 = sum(par_score)

        self.labl_score.text=str(psp1)



class GameScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Objetos
        self.first_layout = BoxLayout()
        self.first_layout.orientation = "vertical"
        self.first_layout.size_hint = (0.4, 1)
        self.first_layout.pos_hint = {"x": 0.3, "y": 0.1}
        self.add_widget(self.first_layout)

        self.labl1 = Label(text="Pantalla \n#2",
                           font_size=30)
        self.first_layout.add_widget(self.labl1)

        # Navegacion
        self.nav_layout = BoxLayout()
        self.nav_layout.orientation = "horizontal"
        self.nav_layout.size_hint = (1, 0.08)
        self.add_widget(self.nav_layout)

        self.labl_blank = Label()
        self.nav_layout.add_widget(self.labl_blank)

        self.bot3 = Button(text="Home",
                           shorten=True)
        self.nav_layout.add_widget(self.bot3)
        # evento para cambiar de pantalla
        self.bot3.bind(on_press=self.swap_home)

        self.bot4 = Button(text="Siguiente",
                           shorten=True)
        self.nav_layout.add_widget(self.bot4)

    def swap_home(self, _):
        main_app.screen_manager.current = "home"


class TestApp(App):
    def build(self):
        # screen manager para cambiar screen
        self.screen_manager = ScreenManager()
        self.screen_manager.transition = FadeTransition()

        # home screen config
        self.home_screen = HomeScreen()
        screen = Screen(name="home")
        screen.add_widget(self.home_screen)
        self.screen_manager.add_widget(screen)

        # second screen config
        self.game_screen = GameScreen()
        screen = Screen(name="game")
        screen.add_widget(self.game_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    main_app = TestApp()
    main_app.run()
