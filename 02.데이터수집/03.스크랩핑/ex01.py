import requests
from bs4 import BeautifulSoup

url ='https://www.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

title = soup.title
print(1, title.get_text())

a = soup.a
print(2, a)
print(3, a.span.get_text())
print(4, a.attrs)
print(5, a['href'])