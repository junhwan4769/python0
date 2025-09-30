from db import *
from classes import *

def sale_list(value):
    try:
        sql = 'select * from view_sale where code like %s or name like %s'
        value = f'%{value}%'
        cursor.execute(sql, (value, value))
        rows = cursor.fetchall()
        if rows != None:
            sales = []
            for row in rows:
                sale = Sale()
                sale.seq = row['seq']
                sale.code = row['code']
                sale.name = row['name']
                sale.date = row['fdate']
                sale.price = row['price']
                sale.qnt = row['qnt']
                sale.sum = row['qnt'] * row['price']
                sales.append(sale)
            return sales 
    except Exception as error:
        print('매출목록오류:', error)

def sale_insert(sale):
    try:
        sql='insert into sale(code, date, qnt, price) values(%s, now(), %s, %s)'
        cursor.execute(sql, (sale.code, sale.qnt, sale.price))
        con.commit()
        print('매출등록완료')
    except Exception as error:
        print('매출검색오류:', error)


if __name__=='__main__':
    sales = list()
    for sale in sales:
        sale.print()