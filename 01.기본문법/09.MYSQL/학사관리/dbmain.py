from function import *
from db import *
import os
from dept import *

while True:
    os.system('cls')
    menuPrint('학사관리')
    menu = input('메뉴선택>')
    if menu =='0':
        cursor.close()
        con.close()
        print('프로그램 종료')
        break
    elif menu =='6':
        menuDept()
    elif menu =='1':
        student = Student()
        student.id = newID()
        print(f'학생학번>{student.id}')
        student.name = input('학생 이름>')
        if student.name == '': 
            print('학생 이름은 반드시 입력하시오')
            continue
        student.code = inputCode('학생학과>', 1)
        insert(student)

    elif menu =='2':
        while True:
            value = input('검색어>')
            if value =='': break
            students = search(value)
            if len(students) == 0:
                print('검색된 학생이 없습니다.')
            else:
                for student in students:
                    student.print()
    elif menu =='3':
        keys =['id', 'name', 'dname']
        while True:
            key = inputNum('1.학번순|2.이름순|3.학과순>')
            if key =='': break
            elif key<1 or key>3:
                print('1~3 숫자를 입력하시오')
                continue
            students = list(key)
            for student in students:
                student.print()
              
    elif menu =='4':
        id = input('삭제할 학생 번호>')
        if id =='': continue
        student = read(id)
        if student == None:
            print('삭제할 학생이 없습니다.')
        else: 
            student.print()
            sel = input('삭제하실래요? (Y) >')
            if sel == 'Y' or sel == 'y':
                delete(id)
                input('아무 키나 누르세요')
    elif menu =='5':
        id = input('수정할 학생 번호>')
        student = read(id)
        if student == None:
            print('수정할 학생이 없습니다')
        else:
            student.print()
            name = input(f'학생이름:{student.name}>')
            if name != '': student.name = name
            code = inputCode(f'학과코드:{student.code}>', 5)
            if code != '': student.code = code
            update(student)
        input('아무키나 누르세요')
    else:
        print('0~5번 사이의 숫자 입력하시오')