from kivy.core.window import Window
from kivy.core.audio import SoundLoader

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

        #sound timer
        self.sound = SoundLoader.load('timer.wav')


        # Set font size of the label based on the screen height
        label_font_size = int(Window.height * 0.1)
        self.label = Label(text='', font_size=label_font_size, halign='center')

        # Set size of the button based on the screen width
        button_size = int(Window.width * 0.15)
        button = Button(text='Iniciar', size_hint=(None, None), size=(button_size, button_size))
        button.bind(on_press=self.on_button_press)

        self.progress_bar = ProgressBar(max=5, value=5, width=1)

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
        self.sound.play()
        self.label.text = self.get_random_letter()
        self.time_left = 4
        self.progress_bar.value = 4
        Clock.unschedule(self.update_time_left)
        Clock.schedule_interval(self.update_time_left, 1)


if __name__ == '__main__':
    TestApp().run()
