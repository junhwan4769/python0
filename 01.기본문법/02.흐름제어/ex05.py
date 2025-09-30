names = ['홍길동', '심청이', '강감찬', '이순신']
no=1
for name in names:
    print(f'{no}:{name}')
    no +=1

print('-'*50)
for index, name in enumerate(names):
    print(f'{index}:{name}')

print('-'*50)
for index, name in enumerate(names):
    print(f'{index+1}:{name}') #index에 +1 안하면 0번부터 시작.

print('-'*50)
for index in range(len(names)):
    print(f'{index+1}:{names[index]}')