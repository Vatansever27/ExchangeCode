from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import requests

def get_exchange_rate():
    API_KEY = "8ef419795da48895dfe85ff391624958"
    API_URL = "http://data.fixer.io/api/latest?access_key="
    API_REQUEST = "{}{}".format(API_URL, API_KEY)
    result = requests.get(API_REQUEST).json()
    usd_rate = -1
    try_rate = -1
    cny_rate = -1
    bit_rate = -1
    gold_rate = -1

    if (result["success"]):
        usd_rate = result["rates"]["USD"]
        try_rate = result["rates"]["TRY"]
        cny_rate = result["rates"]["CNY"]
        eur_rate = result["rates"]["EUR"]
        bit_rate = result["rates"]["BTC"]
        gold_rate = result["rates"]["XAU"]

    print(usd_rate,try_rate,cny_rate,eur_rate,bit_rate,gold_rate)
    return usd_rate, try_rate, cny_rate, eur_rate,bit_rate,gold_rate

class giris(GridLayout):  # Fonksiyonlar hakkında setter parametresini öğrenmek için sor
    def __init__(self, **kwargs):
        super(giris,self).__init__(**kwargs)

        self.cols = 2
        self.mıktar = TextInput(multiline = False)
        self.add_widget(self.mıktar)

        self.sonuc = Widget
        self.sonuc = Label(text="Sonuç")
        self.add_widget(self.sonuc)

        self.button1 = Button(text= "TL -> Dolar",font_size = 42)
        self.button1.bind(on_press=self.cevir_tl_dolara)
        self.add_widget(self.button1)

        self.button2 = Button(text= "Dolar -> TL",font_size = 42)
        self.button2.bind(on_press=self.cevir_dolar_tlye)
        self.add_widget(self.button2)

        self.button3 = Button(text= "Yuen -> TL",font_size = 42)
        self.button3.bind(on_press=self.cevir_yuen_tlye)
        self.add_widget(self.button3)

        self.button4 = Button(text= "TL -> Yuen",font_size = 42)
        self.button4.bind(on_press=self.cevir_tl_yuen)
        self.add_widget(self.button4)

        self.button5 = Button(text= "Euro -> TL",font_size = 42)
        self.button5.bind(on_press=self.cevir_euro_tlye)
        self.add_widget(self.button5)

        self.button6 = Button(text= "TL -> Euro",font_size = 42)
        self.button6.bind(on_press=self.cevir_tl_euro)
        self.add_widget(self.button6)

        self.button8 = Button(text= "Gram Altın?",font_size = 42)
        self.button8.bind(on_press=self.gold_tlye)
        self.add_widget(self.button8)

        self.button9 = Button(text= "TL -> Altın",font_size = 42)
        self.button9.bind(on_press=self.tlden_gold)
        self.add_widget(self.button9)

        self.button7 = Button(text= "BitCoin",font_size = 42)
        self.button7.bind(on_press=self.bitcoin)
        self.add_widget(self.button7)

        self.button11 = Button(text= "Temizle",font_size = 42)
        self.button11.bind(on_press=self.silgi)
        self.add_widget(self.button11)

    def çevir(self, mıktar, çeviren, çevrilen):
        sonuc = "Wrong Currencies"
        usd_rate, try_rate, cny_rate, eur_rate, bit_rate, gold_rate = get_exchange_rate()
        if (çeviren == "TL" and çevrilen == "USD"):
            sonuc = mıktar * (usd_rate/try_rate)
        elif (çeviren == "USD" and çevrilen == "TL"):
            sonuc = mıktar * (try_rate/usd_rate)

        elif (çeviren == "TL" and çevrilen == "CNY"):
            sonuc = mıktar * (cny_rate/try_rate)
        elif (çeviren == "CNY" and çevrilen == "TL"):
            sonuc = mıktar * (try_rate/cny_rate)

        elif (çeviren == "TL" and çevrilen == "EUR"):
            sonuc = mıktar * (eur_rate/try_rate)
        elif (çeviren == "EUR" and çevrilen == "TL"):
            sonuc = mıktar * (try_rate/eur_rate)

        elif (çeviren == "TL" and çevrilen == "XAU"):
            sonuc = mıktar * (gold_rate/try_rate)
        elif (çeviren == "XAU" and çevrilen == "TL"):
            sonuc = mıktar * (try_rate/gold_rate)

        elif (çeviren == "BTC" and çevrilen == "TL"):
            sonuc = mıktar * (try_rate/bit_rate)


        return sonuc

    def cevir_tl_dolara(self, button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="TL", çevrilen="USD"))
    def cevir_dolar_tlye(self, button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="USD", çevrilen="TL"))


    def cevir_yuen_tlye(self, button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="TL", çevrilen="CNY"))
    def cevir_tl_yuen(self, button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="CNY", çevrilen="TL"))


    def cevir_euro_tlye(self, button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="TL", çevrilen="EUR"))
    def cevir_tl_euro(self, button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="EUR", çevrilen="TL"))

    def gold_tlye(self,button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="XAU", çevrilen="TL"))

    def tlden_gold(self,button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="TL", çevrilen="XAU"))

    def bitcoin(self,button):
        mıktar = float(self.mıktar.text)
        self.sonuc.text = str(self.çevir(mıktar, çeviren="BTC", çevrilen="TL"))

    def silgi(self,button):
        self.sonuc.text = str ("Temizlendi")
        self.mıktar.text = str("")

class Exchange(App):
    def build(self):
        return giris()

if __name__ == "__main__":
    Exchange().run()
