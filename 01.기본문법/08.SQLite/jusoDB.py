import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

class Person:
    def __init__(self):
        self.seq = 0 
        self.name = '홍길동'
        self.address = '경기도 광명시'

    def print(self):
        print(f'번호:{self.seq}, 이름:{self.name}, 주소:{self.address}')

#목록
def list():
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'select seq, name, address from juso'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows 

#검색
def search(value):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where name like ? or address like ?"
    value = f'%{value}%'
    cursor.execute(sql, (value, value,))
    rows = cursor.fetchall()
    return rows

#읽기
def read(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where seq=?"
    cursor.execute(sql, (seq,))
    row = cursor.fetchone()
    cursor.close()
    con.close()
    return row

#삭제
def delete(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "delete from juso where seq=?"
    cursor.execute(sql, (seq,))
    con.commit()
    cursor.close()
    con.close()

#입력
def insert(person):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "insert into juso(name, address) values(?,?)"
    cursor.execute(sql, (person.name, person.address, ))
    con.commit()
    cursor.close()
    con.close()

#수정
def update(person):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "update juso set name=?, address=? where seq=?"
    cursor.execute(sql, (person.name, person.address, person.seq ))
    con.commit()
    cursor.close()
    con.close()


if __name__ =='__main__':
    # person = Person()
    # person.seq = 1
    # person.print()

    # rows = list()
    # for row in rows:
    #     person = Person()
    #     person.seq = row[0]
    #     person.name = row[1]
    #     person.address = row[2]
    #     person.print()

    # rows = search('경기')
    # for row in rows:
    #     person = Person()
    #     person.seq = row[0]
    #     person.name = row[1]
    #     person.address = row[2]
    #     person.print()

    # row = read(1)
    # person = Person()
    # person.seq = row[0]
    # person.name = row[1]
    # person.address = row[2]
    # person.print()

    # seq = input('삭제할 번호>')
    # row = read(seq)
    # if row == None : 
    #     print('해당 삭제 번호가 없습니다.')
    # else:
    #     person = Person()
    #     person.seq = row[0]
    #     person.name = row[1]
    #     person.address = row[2]
    #     person.print()
    #     delete(seq)
    #     rows=list()
    #     print(f'데이터갯수:{len(rows)}')

    # person = Person()
    # rows=list()
    # print(f'입력전 데이터 갯수:{len(rows)}')
    # person.name = input('입력할 이름>')
    # person.address = input('입력할 주소>')
    # insert(person)
    # rows=list()
    # print(f'입력후 데이터 갯수:{len(rows)}')

    person = Person()
    person.seq = int(input('수정할 번호>'))
    row = read(person.seq)
    if row == None:
        print('해당 수정번호가 없습니다')
    else: 
        person.name = row[1]
        person.address = row[2]
        name = input(f'이름:{person.name}>')
        if name !='': person.name = name 

        address = input(f'이름:{person.address}>')
        if address !='': person.address = address
        update(person)
        print('수정 완료')

