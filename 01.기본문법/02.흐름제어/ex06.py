no= int(input('학생수>'))

names = []
for i in range(no): #0부터 no-1까지
    name=input('이름>')
    names.append(name)

for i in range (len(names)):
    print(names[i], end=',')

for name in names:
    print(name)

for i, name in enumerate(names):
    print(i, name, end= ',')