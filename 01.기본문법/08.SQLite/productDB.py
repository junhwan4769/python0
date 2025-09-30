import os
import sqlite3
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

class Product:
    def __init__(self):
        self.code=0
        self.name=''
        self.price=0

    def print(self):
        print(f'코드:{self.code}, 이름:{self.name}, 가격:{self.price:,}원')

def rowPrint(row):
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()
        return product

def rowPrint2(row):
    if row == None:
        print('해당 상품이 없습니다.')
    else:
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()
        return product


def list(type): #type=1 코드순, type=2 이름순, type=3 최저가, type=4 최고가
    con = sqlite3.connect(db_name) # 데이터베이스 오픈
    cursor=con.cursor() #커서 오픈
    sql= 'select * from product'
    if type==1:
        sql += ' order by code'
    if type==2:
        sql += ' order by name'
    if type==3:
        sql += ' order by price'
    if type==4:
        sql += ' order by price desc'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

def list_test(type):
    rows = list(type)
    for row in rows:
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()

def insert(product):
    con=sqlite3.connect(db_name)
    cursor=con.cursor()
    sql= 'insert into product(name, price) values(?,?)'
    cursor.execute(sql, (product.name, product.price,))
    con.commit()
    cursor.close()
    con.close()

def insert_test():
    product = Product()
    product.name = input('상품 이름>')
    product.price = int(input('상품 가격>'))
    insert(product)

def read(code):
    con =sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'select * from product where code = ?'
    cursor.execute(sql, (code,))
    row = cursor.fetchone()
    cursor.close()
    con.close()
    return row

def search(name):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'select * from product where name like ?'
    cursor.execute(sql, (f'%{name}%', ))
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

def delete(code):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'delete from product where code=?'
    cursor.execute(sql,(code,))
    con.commit()
    cursor.close()
    con.close()

def update(product):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql ='update product set name=?, price=? where code=?'
    cursor.execute(sql, (product.name, product.price, product.code,))
    con.commit()
    cursor.close()
    con.close()

def update_test():
    code = int(input('상품코드>'))
    row = read(code)
    product = rowPrint(row)
    if product != None:
        name = input(f'상품이름: {product.name}>')
        if name != '' : product.name = name
        price = input(f'상품가격:{product.price:,}>')
        if price != '': product.price = int(price)
        update(product)
        print('수정 완료')

def delete_test():
    code = int(input('상품코드>'))
    row = read(code)
    if row == None:
        print('상품 코드가 없습니다')
    else:
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()
        delete(code)

def search_test():
    while True:
        name = input('검색할 상품 이름>')
        if name =='': break
        rows = search(name)
        for row in rows:
            product = Product()
            product.code = row[0]
            product.name = row[1]
            product.price = row[2]
            product.print()

def read_test():
    code = int(input('상품코드>'))
    row = read(code)
    if row == None:
        print('상품 코드가 없습니다')
    else:
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()

if __name__=='__main__':
        # insert_test()

    # list_test(1)

    # while True:
    #     read_test() 

    # search_test()
    # delete_test()

    # rows = list(4)
    # for row in rows:
    #     rowPrint(row)

    update_test()