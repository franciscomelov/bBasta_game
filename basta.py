from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from random import choice as random_choice
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        self.used_letters = set()
        self.time_left = 5
        self.category = ""
        layout = BoxLayout(orientation='vertical')

        # sound timer
        self.sound = SoundLoader.load('timer.wav')

        # colores
        Window.clearcolor = (0, 0.3, 0.3, 1)  # Color de fondo tipo pizarrón

        # Set font size of the label based on the screen height
        label_font_size = int(Window.height * 0.1)
        self.label = Label(text='', font_size=label_font_size, halign='center')

        self.progress_bar = ProgressBar(max=5, value=5, width=1)

        # Set size of the button based on the screen width
        button_size = int(Window.width * 0.15)

        button = Button(text='Iniciar', size_hint=(1, None), size=(button_size, button_size))
        button.background_color = (0.5, .5, .5, .5)
        button.bind(on_press=self.on_button_press)

        # Add a new button to select a new category
        category_button = Button(text='Nueva categoría', size_hint=(1, None), size=(button_size * 2, button_size))
        category_button.background_color = (0.5, .5, .5, .5)
        category_button.bind(on_press=self.select_new_category)

        layout.add_widget(self.label)
        layout.add_widget(self.progress_bar)
        layout.add_widget(button)
        layout.add_widget(category_button)
        return layout

    def get_random_letter(self):
        letters = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        unused_letters = letters - self.used_letters
        if not unused_letters:
            self.used_letters = set()
            unused_letters = letters
        letter = random_choice(list(unused_letters))
        self.used_letters.add(letter)
        return letter

    def select_new_category(self, instance):
        categories = ['pais', 'nombre', 'apellido', 'flor o fruto', 'color', 'cosa', 'animal', 'ciudad o pais', 'deporte', 'cancion', 'celebridad', 'libro', 'pelicula']
        self.category = random_choice(categories)
        self.label.text = f'Categoría: {self.category}'

    def update_time_left(self, dt):
        self.time_left -= 1
        self.progress_bar.value = self.time_left
        if self.time_left == 0:
            self.label.text = '¡PERDISTE!'

    def on_button_press(self, instance):
        self.sound.play()
        self.label.text = f'Categoría: {self.category}\n{self.get_random_letter()}'
        self.time_left = 5
        self.progress_bar.value = 5
        Clock.unschedule(self.update_time_left)
        Clock.schedule_interval(self.update_time_left, 1)


if __name__ == '__main__':
    TestApp().run()
