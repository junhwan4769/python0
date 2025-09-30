import requests

url = 'https://ssl.pstatic.net/melona/libs/1544/1544465/ee83fc320714c60a0dcc_20250829121023409.jpg'
res = requests.get(url)

file_name = 'data/naver.jpg'
with open(file_name, 'wb') as file:
    file.write(res.content)