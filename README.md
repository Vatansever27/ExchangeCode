# ExchangeCode

ExchangeCode python kullanılarak yazılmış bir kivy uygulamasıdır.
Döviz işlemlerini güncel olarak fixer.io sitesinden json fonksiyonu sayesinde almaktayız

Nasıl Çalışır ? Class Exchange sınıfı ile uygulamamız çalışır.
                Class giris İse Uygulamanın algoritma kısmıyla ilgilenir.
                Class get_exchange_rate fixer.io sitesinden güncel olarak döviz verilerini çekmektedir.
İşleme Tarzı =  get_exchange_rate (Verileri Alır) -> giris (Alınan değerleri algoritmadan geçirir) -> Exchange (Uygulamayı                      çalıştırır)


