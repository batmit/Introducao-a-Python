import requests
from bs4 import BeautifulSoup as bs
url = 'http://www.coindesk.com/price/bitcoin'
r = requests.get(url)
soup = bs(r.content, "html.parser")
price = soup.find("div", {"class":"price-large"})
print("Bitcoin: ", price.text) # print only the text

print("-" *30)

url = 'https://www.infomoney.com.br/cotacoes/vale-vale3/historico/'
r = requests.get(url)
soup = bs(r.content, "html.parser")
price = soup.find("div", {"class":"value"})
print("Vale3: ", price.text) # print only the text

print("-" * 30)

url = 'https://www.infomoney.com.br/cotacoes/itau-unibanco-itub4/historico/'
r = requests.get(url)
soup = bs(r.content, "html.parser")
price = soup.find("div", {"class":"value"})
print("ITUB4: ", price.text) # print only the text

print("-" * 30)

url = 'https://www.infomoney.com.br/cotacoes/fundos-imobiliarios-knip11/grafico/'
r = requests.get(url)
soup = bs(r.content, "html.parser")
price = soup.find("div", {"class":"value"})
print("KNIP11: ", price.text) # print only the text

print("-" *30)


url = 'https://www.infomoney.com.br/cotacoes/itausa-itsa4/'
r = requests.get(url)
soup = bs(r.content, "html.parser")
price = soup.find("div", {"class":"value"})
print("ITSA4: ", price.text) # print only the text


print("-" *30)


url1 = 'https://darksky.net/forecast/-19.5298,-42.6253/ca24/en'
r1 = requests.get(url1)
soup1 = bs(r1.content, "html.parser")
price1 = soup1.find("span", {"class":"summary swap"})
print(price1.text)

print("-" *30)


a = input("Tudo blz? ")
