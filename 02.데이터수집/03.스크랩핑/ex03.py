import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

top5 = soup.find('div', attrs={'class':"aside_area aside_popular"})
names = top5.find_all('a')
print(len(names))

for name in names:
    print(name.get_text())
