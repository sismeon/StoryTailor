import database.manager

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
# from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

from ui import game, login

Builder.load_file('./main.kv')


class StoryTailorScreenManager(ScreenManager):
    pass


class StoryTailorApp(App):
    def build(self):
        return StoryTailorScreenManager()


if __name__ == "__main__":
    StoryTailorApp().run()
    Window.size = (1000, 667)