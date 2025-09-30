#딕셔너리 dict
students={1:'홍길동', 2:'강감찬', 3:'이순신'}
print(1, type(students))

#dict 검색
print(2, students.get(2), students[1])
print(3, students.get(5))

#dict 입력
students[4]= '유재석'
print(4, students)

#dict 수정
students[1]='김길동'
print(5,students)

#dict 삭제
students.pop(2)
print(6, students)

#dict 전부 삭제
students.clear()
print(7, students)