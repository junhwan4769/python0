#문자열 함수
#남자?
jumin = '990120-2155011'
#index   01234567
gender = jumin[7]
result = gender=='1' or gender=='3'
print(f'{gender} 결과는 {result}')

yy=jumin[0:2] #index 0부터 1까지
print(yy)

mm=jumin[2:4] #index 2부터 3까지
print(mm)

dd=jumin[4:6] #index 4부터 5까지
print(dd)

print(f'{yy}년{mm}월{dd}일')

print(jumin[-7:]) 
print(jumin[-1:]) 