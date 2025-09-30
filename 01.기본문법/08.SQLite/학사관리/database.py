import os, sqlite3
path = os.path.dirname(os.path.realpath(__file__))
# print(path)
db_name = path + '/haksa.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

class Dept:
    def __init__(self):
        self.code = 0
        self.dname = ''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.dept = 0
    
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.dept}) ')

def listDept():
    try:
        sql = 'select * from dept'
        cursor.execute(sql)
        rows = cursor.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.code = row[0]
            dept.dname = row[1]
            list.append(dept)
        return list
    except Exception as error:
        print('학과목록:', error)

def inputDept(title,type):
    depts = listDept()
    for dept in depts:
        print(f'{dept.code}.{dept.dname}', end ='|')
    print()
    codes = [dept.code for dept in depts]

    while True:
        code = input(title)
        if code == ''and type == 5:
            return ''
        if code == ''and type == 1:
            print('학과코드는 반드시 입력하세요')
        elif not code.isnumeric():
            print('학과코드는 숫자로 입력하세요') 
        elif codes.count(int(code))==0:
            print(f'{min(codes)}~{max(codes)}번을 입력하세요')
        else:
            return int(code)

def list():
    try:
        sql = 'select * from vstudent'
        cursor.execute(sql)
        rows = cursor.fetchall()
        list=[]
        for row in rows:
            student = Student()
            student.id = row[0]
            student.dept = row[1]
            student.name = row[2]
            student.dname = row[3]
            list.append(student)
        return list
    except Exception as error:
        print('목록 에러:', error)
    finally:
        cursor.close()
        con.close()

def search(value):
    try:
        sql = 'select * from vstudent where name like ? or id like ? or dname like ?'
        value = f'%{value}%'
        cursor.execute(sql, (value,value,value,))
        rows = cursor.fetchall()
        list=[]
        for row in rows:
            student = Student()
            student.id = row[0]
            student.dept = row[1]
            student.name = row[2]
            student.dname = row[3]
            list.append(student)
        return list
    except Exception as error:
        print('검색 오류', error)
    finally:
        pass

def newID():
    try:
        sql = 'select max(id)+1 from student'
        cursor.execute(sql)
        row = cursor.fetchone()
        new_id= row[0]
        return new_id
    
    except Exception as error:
        print('코드생성:', error)
    finally:
        pass
    

def insert(student):
    try:
        sql = 'insert into student(id, name, dept) values(?,?,?)'
        cursor.execute(sql, (student.id, student.name, student.dept,))
        con.commit()
    except Exception as error:
        print('입력 오류', error)
    finally:
        pass

def read(id):
    try:
        sql = "select id, name, dept, dname from vstudent where id=?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row !=None:
            student = Student()
            student.id = id
            student.name = row[1]
            student.dept = row[2]
            student.dname = row[3]
            return student
    except Exception as error:
        print('학번읽기오류:', error)
    

def delete(id):
    try:
        sql = 'delete from student where id=?'
        cursor.execute(sql, (id,))
        con.commit()
    except Exception as error:
        print('학생삭제오류:', error)


def update(student):
    try:
        sql = 'update student set name=?, dept=? where id =?'
        cursor.execute(sql, (student.name, student.dept, student.id, ))
        con.commit()
    except Exception as error:
        print('학생수정오류:', error)


if __name__=='__main__':
        student=read('2509')
        if student == None:
            print('학생이 없습니다')
        else:
            student.print()

    # value = input('검색어>')
    # students = search(value)
    # if students!=None:
    #     for student in students:
    #         student.print()

    # student = Student()
    # student.id = newID()
    # print(f'학번:{student.id}')
    # student.name = input('이름>')
    # if student.name == '':
    #     print('이름은 반드시 입력하시오')
    # else: 
    #     student.dept = int(input('학과>'))
    # insert(student)

    # row = read(2501)
    # student = Student()

    # if row != None:
    #     student.id = row[0]
    #     student.dept = row[1]
    #     student.name = row[2]
    #     student.dname = row[3]
    #     student.print()
    # else:
    #     print("해당 id에 해당하는 학생 데이터가 없습니다.")
    
        # student = Student()
        # student.id = int(input('수정할 번호>'))
        # row = read(student.id)
        # if row == None:
        #     print('해당 수정번호가 없습니다')
        # else: 
        #         student.dept = row[1]
        #         student.name = row[2]
        #         dept = int(input(f'학과:{student.dept}>'))
        #         if dept !='': student.dept = dept

        #         name = input(f'이름:{student.name}>')
        #         if name !='': student.name = name
        #         update(student)
        #         print('수정 완료')

    # depts = listDept()
    # for dept in depts:
    #     print(f'{dept.code}.{dept.dname}', end ='|')

    # code = inputDept()
    # print('입력한 학과코드:', code)