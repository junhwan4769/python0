import os
from product import *
from sub import *

while True:
    os.system('cls')
    print('--------------------------------')
    print('             상품관리             ')
    print('--------------------------------')
    print('[1] 상품등록')
    print('[2] 상품검색')
    print('[3] 상품목록')
    print('[4] 상품정보수정')
    print('[5] 매출관리')
    print('[0] 프로그램 종료')
    print('--------------------------------')
    menu = input('메뉴 선택>')

    if menu =='0':
        cursor.close()
        con.close()
        print('프로그램 종료')
        break

    elif menu =='1':
        code = inputCode('상품코드>')
        if code == '': continue
        product = read(code)
        if product != None:
            product.print()
            print('이미 등록된 상품입니다')
        else:
            product = Product()
            product.code = code
            product.name = input('상품이름>')
            product.price = inputPrice('상품가격>')
            if product.price == '': product.price = 0
            insert(product)
        input('아무키나 누르세요')

    elif menu =='2':
        while True:
            value = input('검색어>')
            if value == '': break
            products = search(value)
            if len(products) == 0:
                print('검색된 상품이 없습니다')
            else: 
                for product in products:
                    product.print()

    elif menu =='3':
        products = product.list()
        for product in products:
            product.print()
        input('아무키나 누르세요')

    elif menu =='4':
        code = inputCode('상품코드>')
        if code =='': continue
        product = read(code)
        if product == None:
            print('등록되지 않은 상품입니다')
        else:
            name = input(f'상품이름:{product.name}>')
            if name != '': product.name = name
            price = inputPrice(f'상품가격:{product.price:,}원>')
            if price != '': product.price = price
            product.print()
            sel = input('수정하실래요? (Y) >')
            if sel == 'Y' or sel == 'y':
                update(product)
            else: 
                print('수정이 취소되었습니다')

        input('아무키나 누르세요')

    elif menu =='5':
        saleMenu()
        input('아무키나 누르세요')

    else:
        print('0~5 숫자를 입력하시오')
    
