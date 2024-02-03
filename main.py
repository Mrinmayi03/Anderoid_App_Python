import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

#This is the specific kivy version that we need(Different for different phones)
kivy.require('1.9.0')


class MyRoot(BoxLayout):
    #Generate number function:
    
    def __init__(self):
        super(MyRoot , self).__init__()
        
    def generate_number(self):
        self.random_label.text = str(random.randint(0 , 1000))

#creating a class
class MKApp(App):
    
    #This function is essentially used to return the UI
    def build(self):
        return MyRoot()


mkapp = MKApp()
mkapp.run()