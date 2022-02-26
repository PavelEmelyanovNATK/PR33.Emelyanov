from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button 
from kivy.lang import Builder 
from kivy.properties import StringProperty 

Builder.load_file("main.kv")

class StartScreen(FloatLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class Program(App): 
    def build(self):
        return StartScreen()

if __name__ in ('__main__'): 
    Program().run()