import requests

url = "http://data.fixer.io/api/latest?access_key=7f1041bd3ff82ed834a666c50abfe31d"

birinci_döviz = input("Birinci: ")
ikinci_döviz = input("İkinci: ")
miktar = float(input("Miktar: "))
response = requests.get(url+birinci_döviz)

json_verisi = response.json()

print(json_verisi["rates"][ikinci_döviz] * miktar)
