from kivy.app import App
import requests
from bs4 import BeautifulSoup
from kivy.uix.boxlayout import BoxLayout
import kivy
from kivy.lang import Builder
kivy.require("1.10.1")

Builder.load_file("Dolar-Kuru-Slider.kv")

class Kontrol(BoxLayout):
    def __init__(self):
        super(Kontrol,self).__init__()

    def btn_tık(self,):
        self.label.text = "He"

        #self.data = requests.get("https://www.bloomberght.com/doviz/dolar")

        #self.soup = BeautifulSoup(data.text,"html.parser")

        #self.a = soup.find_all("span",{"class","piyasaDataValues"})


        #liste = []

        #for i in a:
        #    liste.append(i.text)
        #for j in liste:
         #   print(j)
        #self.x = print(j)
class Uygulama(App):

        def build(self):
            return Kontrol()


kont = Uygulama()

kont.run()
