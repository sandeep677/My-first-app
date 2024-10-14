from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
Window.clearcolor=(1,1,1,1)
class LoginPage(Screen):
    pass

class MainPage(Screen):
    pass
 
class Manager(ScreenManager):
    pass

class Myapp(App):
    def build(self):
        pass
    
Myapp().run()