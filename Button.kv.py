from bs4 import  BeautifulSoup
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyWindowsApp(App):
    def __init__(self):
        super(MyWindowsApp,self).__init__()

        self.button = Button(text = "Çevir")
        self.label = Label(text = "Bitcoin")

    def build(self):
        self.button.bind(on_press = self.clk)
        layout = BoxLayout()
        layout.orientation = "vertical"
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        return layout

        self.url = "http://data.fixer.io/api/latest?access_key=7f1041bd3ff82ed834a666c50abfe31d"
        self.response = requests.get(url)
        self.html_icerigi = response.content
        self.soup = BeautifulSoup(self.html_icerigi,"html.parser")
        print(soup.find_all("span",{"class":"menu-row2"}))

    def clk(self,obj):


windows = MyWindowsApp

windows().run()
