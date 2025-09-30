from function import *
from product import Product
from sale import Sale


products = [
    {'code':'001', 'name':'LG 냉장고', 'price':250},
    {'code':'002', 'name':'LG 세탁기', 'price':180},
]

sale = []

def search(code):
    for p in products:
        if code == p['code']:
            return p 
        
def max_seq():
    seqs = []
    for s in sale:
        seqs.append(s['seq'])
    if len(seqs) == 0:
            return 0
    else:
            return max(seqs)

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택>')

    if menu == '0':
        print('프로그램 종료')
        break
    
    elif menu == '1':
        code = input('상품 코드>')
        if code == '': continue
        p = search(code)
        if p == None :
            print(f"{code}번 상품을 찾을 수 없습니다.")
        else: 
            name = p['name']
            price = p['price']
            print(f'상품 이름:{name},상품 가격:{price}')
            qnt = inputNum('판매수량>')
            if qnt == '': continue
            s = Sale(code, name, price, qnt)
            s.seq = max_seq()+1
            sale.append(s.dict())
            print('등록 완료')

    elif menu == '3':
         for s in sale:
            print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
            print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")

    elif menu == '2':
         name = input('검색이름>')
         for s in sale :
              if (s['name'].find(name.upper())) !=-1 :
                   print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
                   print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")

    elif menu == '4':
         seq = inputNum('삭제할 번호>')
         if seq == '': continue
         for idx, s in enumerate(sale):
              if s['seq'] == seq :
                   print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원,", end="")
                   print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
                   sel = input('삭제하실래요? (Y)')
                   if sel == "Y" or sel == "y":
                        sale.pop(idx)
                        print('삭제 완료')
                   
    elif menu == '5':
         seq = inputNum('수정할 번호>')
         if seq == '': continue
         for s in sale:
              if seq == s['seq']:
                   print(f'상품코드:{s['code']}')
                   print(f'상품이름:{s['name']}')
                   print(f'판매일:{s['date']}')
                   qnt = inputNum(f'판매수량:{s['qnt']}>')
                   if qnt == '': s['qnt'] = qnt
                   print('매출수정완료')

                   
         