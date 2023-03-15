from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import itertools


class Screen(BoxLayout):

    def __init__(self, **kwargs ):
        super(Screen, self).__init__(**kwargs)
        self.orientation = "vertical"
        cuvinte = " "
        boxlayout2 = BoxLayout()
        button = Button()
        txt_instructions = Label(text = "Introduce your letters without any spaces between them")
        self.add_widget(txt_instructions)
        my_user_input = TextInput()
        boxlayout2.add_widget(my_user_input)
        self.add_widget(boxlayout2)

        """THE LABEL HAS ITS SIZE AND POSITION SET TO FOLLOW THE PARENT'S"""
        self.my_output = Label(text_size= (None,None),
                          pos_hint={'center_x': 0.5, 'center_y': .95},
                          size_hint_y=None,
                          size = self.size,
                          height = self.size[1],
                          halign="center",
                          valign = "middle",)

        self.add_widget(self.my_output)

        """BINDING THE LABEL TO THE FUNCTION THAT UPDATES THE SIZE"""
        self.my_output.bind(size=self.setting_function)

        def callback(instance, value):
            cuvinte = " "
            lista2 = []
            lista3 = []
            n = value
            lista = list(n)
            for i in range(len(lista)):
                for word in itertools.permutations(lista):
                    lista2.append(''.join(word[0:len(word)-i]))

            for i in lista2:
                if i not in lista3:
                    lista3.append(i)
            lista3.sort()
            cuvinte = ' '.join(str(e) for e in lista3)
            self.my_output.text = cuvinte

        my_user_input.bind(text=callback)

    def setting_function(self, *args):
        """FUNCTION TO UPDATE THE LABEL TO ADJUST ITSELF ACCORDING TO SCREEN SIZE CHANGES"""
        self.my_output.pos_hint = {'center_x': 0.5, 'center_y': .85}
        self.my_output.text_size=self.size


class MyApp(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    MyApp().run()