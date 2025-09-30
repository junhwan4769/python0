#데이터 상수(정수, 실수 문자열, 불린)
#변수(값을 저장하는 저장소)
#연산자(산술연산자: +,-,*,/,%,//, 관계연산자:>,>=,<,<=,==,!=, 논리연산자:and,or,not)

#list
names= ['홍길동', '심청이','강감찬']

#list 검색
print(1, names[0])

#list 값 입력
names.append('성춘향')
print(2,names)

#list 위치 지정 추가
names.insert(1,'유재석')
print(3, names)

#list 수정
names[1] = '강호동'
print(4, names)

#list 삭제
names.pop(1)
print(5, names)

#데이터 수
print(6, len(names))
print(7, names.count('심청이'))
print(8, type(names))