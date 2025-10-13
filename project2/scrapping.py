import requests 
from bs4 import BeautifulSoup
import time

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def weather():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=jMxCEwpzLiwssffFZ5lssssss3V-393638&ackey=hnzsuy01'
    soup = create_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    if temp:
        temp = temp.getText()
    else:
        temp = ''
    return temp

def exchange():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%ED%99%98%EC%9C%A8&oquery=exchage&tqi=jMxXwsqo1fsssMGmOhVsssssteK-062121&ackey=ki1aqwuh'
    soup = create_soup(url)
    rate = soup.find('span', attrs={'class': 'spt_con dw'}).find('strong')
    if rate:
        rate = rate.getText()
    else:
        rate = ''
    return rate

def stock(query):
    url=f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={query}&ackey=i79dfma9'
    soup = create_soup(url)
    price = soup.find('div', attrs = {'class': 'spt_con dw'}).find('strong')
    if price:
        price = price.getText()
    else:
        price = ''
    return price

if __name__ == '__main__':
    # rate = exchange()
    # print(rate)
    price = stock('삼성주식')
    print(price)