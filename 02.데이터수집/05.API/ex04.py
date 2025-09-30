import requests
import os

def getData(query):
    url=f'https://dapi.kakao.com/v2/local/search/keyword.json?query={query}'
    headers = {'Authorization':'KakaoAK 5249841df27f4d2086247de659772b6d'}
    res=requests.get(url, headers=headers)
    data = res.json()['documents']
    return data

if __name__=='__main__':
    os.system('cls')
    print()
    while True:
        query = input('검색어>')
        if query =='': break
        data=getData(query)
        if len(data) ==0:
            print('검색된 내용 없음')
            continue
        for item in data:
            name=item['place_name']
            address=item['address_name']
            phone=item['phone']
            print(name,address,phone)