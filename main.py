import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '1000')

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass


class HistoryWindow(Screen):
    pass


class SettingWindow(Screen):
    pass


# kv = Builder.load_file('runapp.kv')


class RunApp(App):
    # def build(self):
    #    return kv
    pass


runApp = RunApp()
runApp.run()
