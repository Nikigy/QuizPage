from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class QuizPageApp(App):
    pass

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen):
    pass

class Question2Screen(Screen):
    pass

class CorrectScreen(Screen):
    pass

class IncorrectScreen(Screen):
    pass

QuizPageApp().run()