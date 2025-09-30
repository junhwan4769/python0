sum=0
while True:
    num = input('숫자입력>')
    if num == '': #빈칸 엔터 하면
        print('프로그램 종료')
        break
    sum += int(num)  #shift tab 치면 밖으로 빠져나옴

print('합계:', sum)
