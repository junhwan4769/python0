import requests
from bs4 import BeautifulSoup

def weather(city):

    city = city + '날씨'

    url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={city}%EB%82%A0%EC%94%A8&o&tqi=j7PRQspzL8wssjHxl5dssssssJ0-397807&ackey=cf2oyixz'
    res = requests.get(url)
    # print(res)
    soup = BeautifulSoup(res.text, 'lxml')

    summary = soup.find('p', attrs={'class':'summary'}).getText()
    # print(summary)

    #현재온도
    temp = soup.find('div', attrs={'class':'temperature_text'}).strong.contents[1]
    # print(temp)

    #최저온도
    lowest = soup.find('span', attrs={'class':'lowest'}).contents[1].replace('°','')
    # print(lowest)

    #최고온도
    highest = soup.find('span', attrs={'class':'highest'}).contents[1].replace('°','')
    # print(highest)

    print('[오늘날씨]')
    print('-' * 50)
    print(summary)
    print(f'현재온도: {temp}도 (최저:{lowest}도 / 최고:{highest}도)')
    print('-' * 50)

if __name__=='__main__':
    while True:
        city = input('지역명>')
        if city =='':break
        weather(city)