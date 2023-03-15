import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty
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



class QnAWindow(Screen):
    mood = StringProperty('Mood')

    def on_slider_value(self, widget):

        if widget.value < 20:
            self.mood = 'Sad'
        elif widget.value < 40:
            self.mood = 'Negative'
        elif widget.value < 60:
            self.mood = 'Normal'
        elif widget.value < 80:
            self.mood = 'Positive'
        else:
            self.mood = 'Happy'


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
