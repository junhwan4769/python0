from function import *
from productDB import *

while True:
    menuPrint('상품관리')
    menu = input('메뉴 선택>')
    if menu =='0':
        print('프로그램 종료')
        break
    elif menu == '1':
        product = Product()
        product.name = input('상품 이름>')
        if product.name =='': continue
        product.price = inputNum('상품 가격>')
        if product.price =='': product.price=0
        insert(product)
        print('상품 등록 완료')
    elif menu == '2':
        while True:
            value = input('검색어>')
            if value =='':break
            rows = search(value)
            for row in rows:
                rowPrint(row)
    elif menu == '3':
        while True:
            type=inputNum('1:코드순|2.상품이름순|3.최저가|4.최고가|')
            if type=='':break
            rows = list(type)
            for row in rows:
                rowPrint(row)
    elif menu == '4':
        code = inputNum('상품코드>')
        if code == '': continue
        row = read(code)
        product = rowPrint(row)
        sel = input('삭제하실래요? (Y)')
        if sel == 'Y' or sel == 'y':
            delete(code)
            print('상품 삭제 완료')
    elif menu == '5':
        code = inputNum('상품코드>')
        if code == '': continue
        row = read(code)
        if row == None :
            print('해당상품이 없습니다.')
            continue
        product = rowPrint2(row)
        if product != None :
            name = input(f'상품이름:{product.name}>')
            if name != '': product.name = name
            price = input(f'상품가격:{product.price:,}원>')
            if price != '': product.price = price
            sel = input('수정하실래요? (Y)')
            if sel == 'Y' or sel == 'y':
                update(product)
                print('상품 수정 완료')

    else:
        print('0~5번 숫자를 입력하세요')