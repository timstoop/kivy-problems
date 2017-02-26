from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MyScreenManager(ScreenManager):
    pass


class MyFirstScreen(Screen):
    y = 5

    def on_leave(self, *args):
# Here I want to say something like "next screen should have variable x set to my variable y"


class MySecondScreen(Screen):
    pass


class ProblemApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    ProblemApp().run()
