from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Calculadora(BoxLayout):

    def presionar(self, boton):
        """Agrega el texto del botón a la pantalla"""
        pantalla = self.ids.pantalla
        texto = boton.text

        if texto == "C":
            pantalla.text = ""
        else:
            pantalla.text += texto

    def calcular(self):
        """Evalúa la operación escrita"""
        pantalla = self.ids.pantalla
        try:
            resultado = eval(pantalla.text)
            pantalla.text = str(resultado)
        except ZeroDivisionError:
            pantalla.text = "Error (div/0)"
        except Exception:
            pantalla.text = "Error"


class CalculadoraApp(App):
    def build(self):
        return Calculadora()


if __name__=="_main_":
    CalculadoraApp().run()