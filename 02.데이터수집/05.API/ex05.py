import requests
import os

def getData(query):
    url=f'https://dapi.kakao.com/v2/search/image?query={query}'
    headers = {'Authorization':'KakaoAK 5249841df27f4d2086247de659772b6d'}
    res=requests.get(url, headers=headers)
    data = res.json()['documents']
    return data

if __name__=='__main__':
    query='북극곰'
    list = getData(query)
    for item in list:
        image_url=item['image_url']
        res=requests.get(image_url)

        if res.status_code==200:
            index=image_url.rindex('/')
            file_name=image_url[index+1:]
            
            with open(f'data/image/{file_name}', 'wb') as file:
                file.write(res.content)