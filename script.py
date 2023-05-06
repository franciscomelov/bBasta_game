import random
import string
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class TestApp(App):
    def build(self):
        self.used_letters = set()
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='', font_size=50, halign='center')
        button = Button(text='Iniciar', size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def get_random_vowel(self):
        letters = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        unused_letters = letters - self.used_letters
        if not unused_letters:
            self.used_letters = set()
            unused_letters = letters
        letter = random.choice(list(unused_letters))
        self.used_letters.add(letter)
        print(unused_letters)
        return letter

    def on_button_press(self, instance):
        self.label.text = self.get_random_vowel()


if __name__ == '__main__':
    TestApp().run()
