# CUASAY, RUTH T.
# BS INFO TECH 3WMAD2

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (350, 550)


class CalcGridLayout(GridLayout):


    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
