import random
import string
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock


class TestApp(App):
    def build(self):
        self.used_letters = set()
        self.time_left = 5
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='', font_size=50, halign='center')
        self.progress_bar = ProgressBar(max=5, value=5)
        button = Button(text='Iniciar', size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(self.progress_bar)
        layout.add_widget(button)
        return layout

    def get_random_letter(self):
        letters = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        unused_letters = letters - self.used_letters
        if not unused_letters:
            self.used_letters = set()
            unused_letters = letters
        letter = random.choice(list(unused_letters))
        self.used_letters.add(letter)
        print(unused_letters)
        return letter

    def update_time_left(self, dt):
        self.time_left -= 1
        self.progress_bar.value = self.time_left
        if self.time_left == 0:
            self.label.text = 'YOU LOSE!'

    def on_button_press(self, instance):
        self.label.text = self.get_random_letter()
        self.time_left = 5
        self.progress_bar.value = 5
        Clock.unschedule(self.update_time_left)
        Clock.schedule_interval(self.update_time_left, 1)


if __name__ == '__main__':
    TestApp().run()
