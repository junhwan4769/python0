import os
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
        return result['items']
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

    # 절대경로 지정
    abs_dir = r"C:\python0\05.인공지능\data\감성분석"

    # 폴더가 없으면 생성
    if not os.path.exists(abs_dir):
        os.makedirs(abs_dir)

    # 절대경로를 사용하여 파일 경로 지정
    file_path = os.path.join(abs_dir, "news.json")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print(f"파일이 성공적으로 저장되었습니다: {file_path}")
