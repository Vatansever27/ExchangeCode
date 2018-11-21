from kivy.app import App # Use of fields and methods of Kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("sss.kv")

class MyApp(App):
    def build(self):
        return presentation

myApp = MyApp()
myApp.run()
