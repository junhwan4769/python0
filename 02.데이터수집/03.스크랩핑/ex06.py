import requests
from bs4 import BeautifulSoup
import json

file_name = 'data/할리스매장.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='')


title = ['지역명', '매장명', '주소', '전화']

#[할리스 커피] - [Store] - [매장검색]

list = []
for page in range(1, 11):
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=%EC%84%9C%EC%9A%B8&gugun=&store='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    table = soup.find('table', attrs={'class':'tb_store'})
    rows = table.find_all('tr')
    
    for idx, row in enumerate(rows):
        if idx == 0: continue 
        cols = row.find_all('td')
        city = cols[0].getText().strip()
        name = cols[1].getText().strip()
        address = cols[3].getText().replace(',',' ').replace('.','').strip()
        phone = cols[5].getText().strip().replace('.','')
        data = {'no':idx*page,'city':city,'name':name,'address':address, 'phone':phone}
        list.append(data)

file_name='data/hollys.json'
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)
