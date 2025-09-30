##숫자가 입력될 때까지 계속 입력하는 함수
def inputNum(title):
    while True:
        num = input(f"{title}>")
        if num.isnumeric(): 
            return int(num)
        elif num == "":
            return num
        else:
            print("숫자로 입력하세요.")

num = inputNum("숫자로 입력")
print(num, type(num))

##검색함수 (list와 code를 입력받아서 list에서 code를 검색)
def search(list,code):
    for index, item in enumerate(list):
        if item['code'] == code:
            return index
        
sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

# index = search(sale, 1) #sale은 list, 1은 index
# print(index) #결과는 0

index = search (sale, 1)
# index = search(sale,200)
if index == None:
    print('해당 데이터가 없습니다')
else:
    print(sale[index])
