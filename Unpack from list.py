# Как работает распаковка листа на данном примере анпак и флэтпак распакованы в 0 и 1, при этом лист продолжился
news = list(range(21))
unpack, flatpack, *hz = news
print(news)
