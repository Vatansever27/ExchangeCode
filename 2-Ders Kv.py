from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("calisma2.kv")

box = BoxLayout

class yerlesim(box):
    pass

class uygulama(App):

    def build(self):

        return yerlesim()

if __name__ == "__main__":

    uygulama().run()
