#문자열 함수
str = 'python is amazing'
print(1,str.lower()) #소문자
print(2,str.upper()) #대문자
print(3,str.capitalize()) #첫글자 대문자
print(4,str[0].islower()) #첫글자는 소문자인가?
print(5,len(str)) #총 몇 글자인가? length
print(str.replace('Python', '파이썬'))

index = str.index('a') # 문자a의 위치 찾기
print(index)
print(str[index:])

print(6, str.find('a')) # 문자a의 위치 찾기
print(7, str.count('i')) # 문자 i의 개수는?