from kivy.app import App
from kivy.uix.label import Label

class PoducktivApp(App):
    def build(self):
        label = Label(text="Hello, user!")
        return label

PoducktivApp().run()
