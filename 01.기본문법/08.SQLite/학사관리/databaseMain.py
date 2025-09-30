from function import *
from database import *

while True:
    menuPrint('학생관리')
    menu = input('메뉴선택>')
    if menu == '0':
        print('프로그램 종료')
        cursor.close()
        con.close()
        break

    elif menu == '1': #입력
        student = Student()
        student.id = newID()
        print(f'학번>{student.id}')
        while True:
            student.name = input('이름>')
            if student.name == '':
                print('이름은 반드시 입력하시오')
                continue
            else:
                break
        student.dept = inputDept('학과코드>', 1)
        insert(student)
        print('학생 등록 성공')

    elif menu == '2': #검색
        while True:
            value = input('검색어>')
            if value =='': break
            students = search(value)
            if len(students) == 0:
                print('검색결과가 없습니다')
                continue
            for student in students:
                student.print()
            print(f'{len(students)}명의 학생이 존재합니다.\n')

    elif menu == '3': #목록
        students = list()
        for student in students:
            student.print()
        print(f'{len(students)}명의 학생이 존재합니다.')

    elif menu == '4': #삭제
        id = input('삭제할 학번>')
        if id == '': continue
        student = read(id)
        if student == None : 
            print('삭제할 해당 학생이 없습니다.')
        else:
            student.print()
            sel = input('삭제하실겁니까? (Y)')
            if sel == 'Y' or sel == 'y':
                delete(id)
                print('삭제 완료')

    elif menu == '5': #수정
        id = input('학번>')
        if id =='': continue
        student = read(id)
        if student == None:
            print('수정할 학생이 없습니다')
            continue
        student.print()
        name = input(f'이름:{student.name}>')
        if name != '': student.name = name 
        dept = inputDept(f'학과코드:{student.dept}>', 5)
        if dept != '': student.dept = dept
        update(student)
        print('수정 완료')
    else:
        print('0~5번 메뉴를 선택하시오')
