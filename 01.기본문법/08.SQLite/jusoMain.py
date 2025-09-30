from function import *
from jusoDB import *

while True:
    menuPrint('주소관리')
    menu = input('메뉴 선택>')
    if menu =='0':
        print('프로그램 종료')
        break
    elif menu == '1': #입력
        person = Person()
        rows=list()
        person.name = input('입력할 이름>')
        person.address = input('입력할 주소>')
        insert(person)
        rows=list()
        print('입력 완료')
    elif menu == '2': #검색
        while True:
            person = Person()
            person.name = input('검색할 이름>')
            if person.name =='': 
                 break
            if person.name != '':
                for row in rows:
                    person = Person()
                    person.seq = row[0]
                    person.name = row[1]
                    person.address = row[2]
                    person.print()           
    elif menu == '3': #목록
        rows = list()
        for row in rows:
            person = Person()
            person.seq = row[0]
            person.name = row[1]
            person.address = row[2]
            person.print()
    elif menu == '4': #삭제
        seq = input('삭제할 번호>')
        row = read(seq)
        if row == None : 
            print('해당 삭제 번호가 없습니다.')
        else:
            person = Person()
            person.seq = row[0]
            person.name = row[1]
            person.address = row[2]
            person.print()
            sel = input('삭제하실겁니까? (Y)')
        if sel == 'Y' or sel == 'y':
                delete(seq)
                rows=list()
                print('삭제 완료')

    elif menu == '5': #수정
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
    else: 
        print('0~5번 숫자를 입력하세요')