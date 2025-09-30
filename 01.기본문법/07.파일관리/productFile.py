import os
path = os.path.dirname(os.path.realpath(__file__))
# print('현재패스:', path)
file_name = path + '/product.txt'
# print('파일명', file_name)

class Product:
    def __init__(self):
        self.code= 0
        self.name= ''
        self.price= 0
    def print(self):
        print(f"코드:{self.code}, 상품명:{self.name[:20]}, 가격:{int(self.price):,}원")
        print("-" * 70)

#데이터 하나 추가 함수
def fileAppend(product):
    with open(file_name, 'a', encoding= 'utf-8') as file:
        file.write(f'{product.code}, {product.name}, {product.price}\n')

#모든 데이터를 다시 쓰기 함수
def fileWrite(list):
    with open (file_name, 'w', encoding= 'utf-8') as file :
        for product in list:
            file.write(f'{product.code},{product.name},{product.price}\n')

#모든 데이터를 읽는 함수
def fileRead():
    with open(file_name, 'r', encoding= 'utf-8') as file:
        list = []
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
            product = Product()
            product.code = int(items[0])
            product.name = items[1]
            product.price = items[2].replace('\n', '')
            list.append(product)
        return list
    
def delete(code):
    list = fileRead()
    result = [product for product in list if product.code != code]
    fileWrite(result)

def list():
    list = fileRead()
    for product in list:
        product.print()

def append():
    product = Product()
    product.code = 2
    product.name = '베이직북14 사무용 가벼운 노트북 업무용 인강용 영상편집 윈도우11 home'
    product.price = 388000
    fileAppend(product)
    print('등록 성공')

def update():
    code = 1
    list = fileRead()
    result = [product for product in list if product.code == code]
    product = result[0]
    product.name = ''
    product.price = 0
    fileWrite(list)

if __name__ == '__main__':
    pass