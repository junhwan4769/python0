import pymysql

con = pymysql.connect(
    host= 'localhost', 
    user= 'root',
    password='1234',
    db='haksa',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

cursor = con.cursor()

class Dept:
    def __init__(self):
        self.dcode = 0
        self.dname = ''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.code})')
        print('-'* 50)


def list(key):
    try:
        keys=['id', 'name','dname']
        sql = f'select * from vstudent order by {keys[key-1]}'
        cursor.execute(sql)
        rows = cursor.fetchall()
        list = []
        for row in rows:
            student = Student()
            student.id = row['id']
            student.name = row['name']
            student.dname = row['dname']
            student.code = row['code']
            list.append(student)
        return list
    except Exception as error:
        print('학생 목록 오류', error)

def search(value):
    try:
        sql = 'select * from vstudent where id like %s or name like %s or dname like %s'
        value = f'%{value}%'
        cursor.execute(sql, (value,value,value))
        rows = cursor.fetchall()
        if not rows == None:
            list = []
            for row in rows:
                student = Student()
                student.id = row['id']
                student.name = row['name']
                student.code = row['code']
                student.dname = row['dname']
                list.append(student)
            return list
    except Exception as error:
        print('학생검색오류:', error) 

def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as new_id from student'
        cursor.execute(sql)
        row = cursor.fetchone()
        return row['new_id']
    except Exception as error:
        print('새로운 학번 오류:', error)

def listDept():
    try:
        sql = 'select * from dept'
        cursor.execute(sql)
        rows = cursor.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.dcode = row['dcode']
            dept.dname = row['dname']
            list.append(dept)
        return list
    except Exception as error:
        print('학과목록출력오류:',error)

#학과 코드 입력 함수
def inputCode(title, menu):
    list = listDept()
    codes = [dept.dcode for dept in list]
    print('-' * 50)
    for dept in list:
        print(f'{dept.dcode}.{dept.dname}', end= '|') 
    print()
    print('-' * 50)
    while True:
        code = input(title)
        if code =='' and menu == 1: 
            print('학과코드는 반드시 입력하시오')
        elif code == '' and menu == 5:
            return code
        elif not code.isnumeric():
            print('학과코드는 숫자로 입력하시오') 
        elif codes.count(int(code))==0:
            print(f'{min(codes)}~{max(codes)} 코드번호를 입력하시오')
        else:
            return int(code)
        
def insert(student):
    try:
        sql = 'insert into student(id, name, code) values(%s, %s, %s)'
        cursor.execute(sql, (student.id, student.name, student.code))
        con.commit()
        print('학생 등록 완료')
    except Exception as error:
        print('학생 등록 오류:', error)

def read(id):
    try:
        sql = 'select * from vstudent where id =%s'
        cursor.execute(sql, (id))
        row = cursor.fetchone()
        if row != None:
            student = Student()
            student.id = row['id']
            student.name = row['name']
            student.code = row['code']
            student.dname = row['dname']
            return student
    except Exception as error:
        print('학생읽기오류:', error)

def delete(id):
    try:
        sql = 'delete from student where id = %s'
        cursor.execute(sql, (id))
        print('학생 삭제 완료')
    except Exception as error:
        print('학생삭제오류:', error)

def update(student):
    try:
        sql = 'update student set name=%s, code=%s where id=%s'
        cursor.execute(sql, (student.name, student.code, student.id))
        con.commit()
        print('학생 수정 완료')
    except Exception as error:
        print('학생수정오류:', error)

#학과등록
def insertDept(dname):
    sql = 'insert into dept(dname) values(%s)'
    cursor.execute(sql, (dname))
    con.commit()
    print('학과등록 완료')

#학과읽기
def readDept(dcode):
    sql = 'select * from dept where dcode=%s'
    cursor.execute(sql, (dcode))
    row = cursor.fetchone()
    dept = Dept()
    dept.dcode = row['dcode']
    dept.dname = row['dname']
    return dept

#학과수정
def updateDept(dept):
    sql = 'update dept set name=%s where dcode=%s'
    cursor.execute(sql, (dept.dname, dept.dcode))
    con.commit()
    print('학과 수정 완료')

if __name__ == '__main__':
    # rows = list()
    # print(len(rows))

    # list = list()
    # for student in list:
    #     student.print() 

    # while True:
    #     value = input('검색어>')
    #     if value =='': break
    #     students = search(value)
    #     if len(students) == 0:
    #         print('검색된 학생이 없습니다.')
    #     else:
    #         for student in students:
    #             student.print()

    # print(f'새로운 학번:{newID()}')
    
    # depts = listDept()
    # for dept in depts:
    #     print(f'{dept.dcode}.{dept.dname}', end ='|')
    # print()
    # print('-' * 50)

    # inputCode('학과코드>', 1)

    # code=inputCode('학과코드>',1)
    # print('입력한 학과코드:', code)

    id = input('학번>')
    student = read(id)
    if student == None:
        print('해당 학생이 없습니다')
    else:
        student.print()