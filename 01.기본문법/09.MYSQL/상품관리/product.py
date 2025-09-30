from db import *
from classes import *

def list():
    try:
        sql = 'select * from product'
        cursor.execute(sql)
        rows = cursor.fetchall()
        products = []
        for row in rows:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']
            products.append(product) 
        return products
    except Exception as error:
        print('상품목록오류:', error)

def insert(product):
    try:
        sql = 'insert into product(code, name, price) values(%s, %s, %s)'
        cursor.execute(sql, (product.code, product.name, product.price))
        con.commit()
        print('상품 등록 완료')
    except Exception as error:
        print('상품등록오류:', error)

def search(value):
    try:
        sql = 'select * from product where code like %s or name like %s'
        cursor.execute(sql, (f'%{value}%', f'%{value}%'))
        rows = cursor.fetchall()
        if rows != None:
            products = []
            for row in rows:
                product = Product()
                product.code = row['code']
                product.name = row['name']
                product.price = row['price']
                products.append(product)
            return products
    except Exception as error:
        print('상품검색오류:', error)

def read(code):
    try:
        sql = 'select * from product where code=%s'
        cursor.execute(sql, (code))
        row = cursor.fetchone()
        if row != None:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']
            return product
    except Exception as error:
        print('상품읽기오류', error)

def inputCode(title):
    while True:
        code = input(title)
        if code == '': return code
        if len(code) !=3:
            print('상품코드는 3자리로 입력하시오')
        elif not code.isnumeric():
            print('상품코드는 숫자로 입력하시오')
        else:
            return code
            
def inputPrice(title):
    while True:
        price = input(title)
        if price =='':
            return ''
        elif not price.isnumeric():
            print('가격은 숫자로 입력하시오')
        else:
            return int(price)
        
def update(product):
    try:
        sql = 'update product set name=%s, price=%s where code=%s'
        cursor.execute(sql, (product.name, product.price, product.code))
        con.commit()
        print('상품 수정 완료')
    except Exception as error:
        print('상품수정오류:', error)

#숫자입력 함수
def inputNum(title):
    while True:
        str = input(title)
        if str.isnumeric():
            return int(str)
        elif str == '':
            return str
        else:
            print('숫자로 입력하시오')
            
if __name__ == '__main__':
    # products = list()
    # for product in products:
    #     product.print()

    # product = Product()
    # product.code = '104'
    # product.name = '엘지 TV'
    # product.price = 2150000
    # insert(product)

    # products = search('냉장고')
    # if len(products) == 0:
    #     print('검색 상품이 없습니다')
    # else:
    #     for product in products:
    #         product.print()

    # product = read('101')
    # if product == None:
    #     print('해당상품이 없습니다')
    # else:
    #     product.print()

    # code = inputCode()
    # print('사용할 수 있는 코드:', code)

    price = inputPrice('상품가격>')
    print('가격:', price)