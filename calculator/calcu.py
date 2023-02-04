## Sample Python application demonstrating the
## How to change button position and size in Kivy.
###################################################
# import modules
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# This layout allows you to set relative coordinates for children.
from kivy.uix.relativelayout import RelativeLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

from kivy.core.window import Window

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', False)
Window.size = (350, 550)

# creating the App class
class Pos_Size_App(App):

    def build(self):
        rl = RelativeLayout(size=(300, 300))
        # creating button
        # size of button is 20 % by height and width of layout
        # position is 'center_x':.7, 'center_y':.5
        b1 = Button(size_hint=(.2, .2),
                    pos_hint={'center_x': .7, 'center_y': .5},
                    text="pos_hint")

        # creating button
        # size of button is 20 % by height and 50 % width of layout
        b2 = Button(size_hint=(1, .1),
                    text="=")

        # creating button
        # size of button is 20 % by height and width of layout
        # position is 200, 200 from bottom left
        b3 = Button(size_hint=(.2, .2),
                    pos=(200, 200),
                    text="pos")

        # adding button to widget
        rl.add_widget(b1)
        rl.add_widget(b2)
        rl.add_widget(b3)

        # returning widget
        return rl


# run the App
if __name__ == "__main__":
    Pos_Size_App().run()
