from function import *
from jusoFile import *

class Product:
    def __init__(self):
        self.code= 0
        self.name= ''
        self.price= 0
    def print(self):
        print(f"코드:{self.code}, 상품명:{self.name[:20]}, 가격:{self.price}만원")

while True:
    menuPrint('주소관리')
    menu = input('메뉴선택>')

    if menu == '0':
        print('프로그램 종료')
        break

    elif menu == '1': #입력
        person = Person()
        person.seq = newSeq()
        print(f'번호>{person.seq}')
        if person.seq == '' : continue
        person.name = input('입력할 이름>')
        if person.name == '' : continue
        person.address = input('입력할 주소>')
        fileAppend(person)
        person.print()

    elif menu == '2': #검색
        while True:
            value = input('검색어>')
            if value =='': break
            list = fileRead()
            result = [person for person in list if person.name.find(value) != -1 or person.address.find(value) != -1]
            if len(result) == 0 : 
                print('검색 내용이 없습니다.')
                continue
            for person in result :
                person.print()

    elif menu == '3': #목록
        list = fileRead()
        for person in list:
            person.print()
    
    elif menu == '4': #삭제
        seq = inputNum('삭제할 번호>')
        list = fileRead()
        result = [person for person in list if person.seq == seq]
        if len(result) == 0:
            print('삭제할 번호가 없습니다')
            continue
        person = result[0]
        person.print()
        sel = input('삭제하실겁니까? (Y)')
        if sel == 'Y' or sel == 'y':
            result = [person for person in list if person.seq != seq]
            fileWrite(result)
            print('삭제 성공')

    elif menu == '5': #수정
        seq = inputNum('수정할 번호>')
        if seq == '': continue
        list = fileRead()
        result = [person for person in list if person.seq == seq]
        if len(result) == 0:
            print('수정할 번호가 없습니다.')
            continue
        person = result[0]
        name = input(f'이름:{person.name}>')
        if name !='': person.name = name
        address = input(f'주소:{person.address}>')
        if address !='': person.address = address
        sel = input('수정하시겠습니까 (Y)')
        if sel == 'Y' or sel == 'y':
            person.print()
            fileWrite(list)
            print('수정완료')


   
        

