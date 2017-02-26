from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty


class MyScreenManager(ScreenManager):
    pass


class MyFirstScreen(Screen):
    pass


class MySecondScreen(Screen):
    pass


class SolutionApp(App):
    score = NumericProperty(0)

    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    SolutionApp().run()