import pandas as pd
import random
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout

Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '1000')

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import calendar
from datetime import date, datetime


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass


def today_question():
    questions = pd.read_csv('data/questions_list.csv')
    ques_id = random.randint(0, len(questions) - 1) + 1
    today_ques = questions.loc[ques_id - 1, 'english']
    return today_ques, ques_id


answers_list = pd.DataFrame(columns=['id', 'date', 'question', 'answer', 'mood'])


class QnAWindow(Screen):
    mood = StringProperty('')

    def on_slider_value(self, widget):

        if widget.value < 20:
            self.mood = 'sad'
        elif widget.value < 40:
            self.mood = 'negative'
        elif widget.value < 60:
            self.mood = 'normal'
        elif widget.value < 80:
            self.mood = 'positive'
        else:
            self.mood = 'happy'

    question, ques_id = today_question()
    answer = ''

    def set_answer(self, ans):
        self.answer = ans
        self.ids.answer.text = self.answer
        self.ids.answer.size_hint = (0.75, 0.05) if self.width < self.height else (0.3, 0.05)

        global answers_list

        answers_list = answers_list.append({'id': self.ques_id, 'date': datetime.today().strftime('%Y-%m-%d'), 'question': self.question, 'answer': self.answer, 'mood': self.mood},
                                           ignore_index=True)
        print(answers_list)


class HistoryWindow(Screen):
    today = date.today()
    year = today.year
    month = today.month
    day = today.day

    if month == 1:
        month_name = 'January'
    elif month == 2:
        month_name = 'February'
    elif month == 3:
        month_name = 'March'
    elif month == 4:
        month_name = 'April'
    elif month == 5:
        month_name = 'May'
    elif month == 6:
        month_name = 'June'
    elif month == 7:
        month_name = 'July'
    elif month == 8:
        month_name = 'August'
    elif month == 9:
        month_name = 'September'
    elif month == 10:
        month_name = 'October'
    elif month == 11:

        month_name = 'November'
    else:
        month_name = 'December'

    today_text = month_name + ' ' + str(year)


'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)
'''


# class SelectDayButton(Button):
#    pass
class SelectDayLayout(RelativeLayout):
    pass


class CalendarBox(GridLayout):
    cols = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):
            b = SelectDayLayout()
            self.add_widget(b)


class SettingWindow(Screen):
    pass


# kv = Builder.load_file('runapp.kv')


class RunApp(App):
    # def build(self):
    #    return kv
    pass


runApp = RunApp()
runApp.run()
