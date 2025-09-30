#list 타입
names =['홍길동','심청이','강감찬']
print(names, type(names))

names.append('박명수') #추가
print(names, type(names))

names.pop() #퇴출
print(names)

names.insert(1,'박명수') #첫번째 자리에 추가 / 홍길동은 0번째 자리.
names.append('박명수') #하나 더 추가
print(names)

print(names.count('박명수')) #박명수는 몇개 있나?
print(names[0]) #맨 앞 자리
print(names[-1]) #마지막 자리
print(names[1:3]) #1번 자리와 2번 자리 까지