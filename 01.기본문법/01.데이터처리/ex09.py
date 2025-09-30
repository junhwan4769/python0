#기본함수
print(1, abs(-5)) #절대값
print(2, pow(4,3)) #4의3승
print(3, max(5,2,10,1,7)) #최대값
print(4, min(5,2,10,1,7)) #최소값
print(5, round(3.14)) #반올림
print(6, round(3.14159, 3)) #반올림해서 셋째 자리까지 출력

from math import *
print(7, floor(4.99)) #소수점 버림 내림
print(8, ceil(3.01)) #무조건 올림
print(9, sqrt(16)) #제곱근

from random import *
print(10, random()) #0이상 1미만
print(11, random() * 10) #0이상 10미만
print(12, int(random() * 10)) #0에서 9까지

print(13, randint(1, 45)) #1에서 45까지