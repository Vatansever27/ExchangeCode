from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder

Builder.load_file("calisma.kv")


class etiket(FloatLayout):
    pass

class uygulama(App):

    def build(self):

        return etiket()

if __name__ == "__main__":

    uygulama().run()
