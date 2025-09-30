#1~100 합계
tot=0
for j in range(1, 101):
    tot +=j #tot=tot+j j를 누적해서 tot
print(tot)

sum=0
for i in range(2,101,2): #2~100 짝수합계
    sum +=i
print(sum)

sum=0
for i in range(1,100,2): #1~99 홀수합계
    sum +=i
print(sum)