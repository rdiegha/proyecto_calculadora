from kivy.app import App
from kivy.uix.label import Label


class CalculadoraApp(App):
    def build(self):
        return Label(text="Calculadora de Notas")


CalculadoraApp().run()