from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class QuizPageApp(App):
    pass

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen):
    pass

class Question2Screen(Screen):
    def check_answer(self):
        user_answer = self.ids.answer.text.lower()  # get the user's input and convert to lowercase
        correct_answer = "pinkerton" 
        if user_answer == correct_answer:
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"

class CorrectScreen(Screen):
    pass

class IncorrectScreen(Screen):
    pass

QuizPageApp().run()