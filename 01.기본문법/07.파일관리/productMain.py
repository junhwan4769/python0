from function import *
from productFile import *

def newCode():
    list = fileRead()
    result = sorted(list, key=lambda product:product.code, reverse = True)
    if len(list) == 0:
        return 1
    else: 
        product = result[0]
        return product.code +1

while True:
    menuPrint('상품관리')
    menu = input('메뉴 선택>')
    if menu == '0':#종료
        print('프로그램을 종료합니다')
        break
    elif menu == '1':#입력
        product = Product()
        product.code = newCode()
        print(f'코드>{product.code}')
        if product.code == '' : continue
        product.name = input('입력할 이름>')
        if product.name == '' : continue
        product.price = input('입력할 가격>')
        fileAppend(product)
        product.print()

    elif menu == '2':#검색
        while True:
            value = input('검색어>')
            if value =='': break
            list = fileRead()
            result = [product for product in list if product.name.find(value) != -1]
            if len(result) == 0 : 
                print('검색 내용이 없습니다.')
                continue
            for product in result :
                product.print()

    elif menu == '3':#목록
            sort = inputNum('1.코드순|2.이름순|3.최저가|4.최고가>')
            if sort == '':break
            list = fileRead()
            result = []
            if sort==1:result = sorted(list, key=lambda product:product.code)
            if sort==2:result = sorted(list, key=lambda product:product.name)
            if sort==3:result = sorted(list, key=lambda product:product.price)
            if sort==4:result = sorted(list, key=lambda product:product.price, reverse=True)
            print()
            for product in result:
                product.print()

    elif menu == '4':#삭제
        code = inputNum('삭제할 코드>')
        list = fileRead()
        result = [product for product in list if product.code == code]
        if len(result) == 0:
            print('삭제할 번호가 없습니다')
            continue
        product = result[0]
        product.print()
        sel = input('삭제하실겁니까? (Y)')
        if sel == 'Y' or sel == 'y':
            result = [product for product in list if product.code != code]
            fileWrite(result)
            print('삭제 성공')

    elif menu == '5':#수정
        seq = inputNum('수정할 번호>')
        if seq == '': continue
        list = fileRead()
        result = [product for product in list if product.code == code]
        if len(result) == 0:
            print('수정할 번호가 없습니다.')
            continue
        person = result[0]
        name = input(f'이름:{product.name}>')
        if name !='': product.name = name
        price = input(f'가격:{product.price}>')
        if price !='': product.price = price
        sel = input('수정하시겠습니까 (Y)')
        if sel == 'Y' or sel == 'y':
            product.print()
            fileWrite(list)
            print('수정완료')
    else:
        print('0~5 숫자를 입력하시오')