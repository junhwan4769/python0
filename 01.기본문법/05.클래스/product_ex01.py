from function import *
from product  import Product

products = [
    {'code':'001','name':'LG 냉장고','price':'250'},
    {'code':'002','name':'LG 세탁기','price':'180'}
]

def search(code):
    for idx, p in enumerate(products):
        if code == p['code']:
            return idx


while True :
    menuPrint('상품관리')
    menu = input('메뉴선택>')

    if menu == "0":
        print('프로그램 종료')
        break

    elif menu == "1": #등록
        code = len(products)+1
        code = f'{code:03d}'
        # code = input('상품코드>')
        print(f'상품코드>{code}')
        name = input('상품이름>')
        if name == '' : continue
        price = inputNum('상품가격>')
        if price == '': price = 0
        p = Product(code, name, price)
        products.append(p.dict())
        print('상품등록 완료')

    elif menu == "2" : #검색
        name = input('검색 이름>')
        for p in products:
            if p['name'].find(name.upper()) != -1:
                print(p['code'],p['name'],p['price'])


    elif menu == "3": #목록
        for p in products:
            print(p['code'],p['name'],p['price'])
        print(f'{len(products)}개 상품이 존재합니다.')

    elif menu == "4" : #삭제
        code = input('삭제 코드>') # ""
        if code == '' : continue
        idx = search(code)
        if idx == None:
                print(f'{code}번 상품이 없습니다.')
        else:
                p = products[idx]
                print(p['code'],p['name'],p['price'])
                sel = input('삭제하시겠습니까? (Y)')
                if sel == 'Y' or sel == 'y':
                    products.pop(idx)
        # for idx ,p in enumerate(products):
        #     if p['code'] == code :
                print('상품 삭제 완료.')

    elif menu == "5": #수정
         code = input('수정 코드>')
         if code == '' : continue
         idx = search(code)
         if idx == None :
              print(f'{code}번 상품이 없습니다.')
              continue
         
         p = products[idx]
         name = input(f'상품 이름:{p['name']}>')
         if name != '': p['name'] = name
         price = inputNum(f'상품가격:{p['price']}>')
         if price != '': p['price'] = price
         print('수정완료')


