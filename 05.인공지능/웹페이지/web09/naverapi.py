import urllib.request
import json

def getNew(query, start, display):
    client_id = "DSISkunI4gxjpwj6Yl6J"
    client_secret = "CxLnF9_VmQ"
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/news.json?query={encText}&start={start}&display={display}" 
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        return result['items'], result['total']
    else:
        print("Error Code:", rescode)
        return None

if __name__ == '__main__':
    query = '인공지능'
    start = 1
    display = 10
    results = []

    while start <= 100:
        news = getNew(query, start, display)
        if news:
            results.extend(news)
        start += display

    print('데이터갯수:', len(results))

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


