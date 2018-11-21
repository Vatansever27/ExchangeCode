import requests
from bs4 import BeautifulSoup

def cd():
    data = requests.get("https://www.bloomberght.com/doviz/dolar")

    soup = BeautifulSoup(data.text,"html.parser")

    a = soup.find_all("span",{"class","piyasaDataValues"})


    liste = []

    for i in a:
#    for j in
        liste.append(i.text)
    for j in liste:
        print(j)

cd()
#a = corba.find_all("div",{"class","line2"})

#<span class="col-lg-4 col-md-6 col-sm-6 col-xs-12 piyasaDataValues">
              #  <span>ALIŞ:</span> <b>5,4721</b>            </span>
#<b>5,4721</b>
#<script async="" src="//www.google-analytics.com/analytics.js"></script>
