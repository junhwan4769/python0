from function import menuPrint, inputNum, grade

scores = [
    {'name':'이순신', 'kor': 90, 'eng':68, 'mat':75},
    {'name':'심청이', 'kor': 100, 'eng':85, 'mat':91},
]
def search(name):
    isFind = False
    for index, s in enumerate(scores):
        if s['name'].find(name) != -1 :
            isFind = True
            tot = s['kor']+s['eng']+s['mat']
            avg = tot/3
            print(index,s['name'], s['kor'], s['eng'], s['mat'], f"{avg:.2f}", grade(avg))

    if isFind==False:
        print("검색 결과가 없습니다.")
    return isFind

while True:
    menuPrint("성적관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print('프로그램을 종료합니다.')
        break

    elif menu == "1": #입력
        name = input("이름>")
        kor = inputNum("국어")
        eng = inputNum("영어")
        mat = inputNum("수학")
        scores.append({"name":name, "kor":kor, "eng":eng, "mat":mat})
        print("입력 성공!")

    elif menu == "3":#목록
        if len(scores)==0: #입력없이 목록 접근 시 
            print("등록된 데이터가 없습니다!")
            continue
        for s in scores:
            tot = s['kor']+s['eng']+s['mat']
            avg = tot/3
            print(s['name'], s['kor'], s['eng'], s['mat'], f"{avg:.2f}", grade(avg))

    elif menu == "2": #검색
        search_name = input('검색할 이름>')
        search(search_name)

    elif menu == "4":#삭제
        del_name = input('삭제할 이름>')
        isFind = search(del_name)
        if isFind == True:
            index = inputNum("삭제번호>")
            scores.pop(index)
            print("삭제완료!")
        # isFind = False
        # for index, s in enumerate(scores):
        #     if s['name'].find(del_name) !=-1: #삭제할 이름 찾은 경우
        #         print(index, s['name'])
        #         isFind = True
        # if isFind:
        #     index = inputNum("삭제번호")
        #     scores.pop(index)
        # else :
        #     print('삭제할 이름이 없습니다.')

    elif menu == "5" : #수정
        edit_name = input("수정이름>")
        isFind = search(edit_name)
        if isFind == True :
            index = inputNum("수정번호")
            s = scores[index]
            name = input(f"수정이름: {s['name']}>")
            if name != "" : s['name'] = name 

            kor = inputNum(f"국어:{s['kor']}")
            if kor!=0: s['kor'] = kor #0으로 입력할 경우

            eng = inputNum(f"영어:{s['eng']}")
            if eng!=0: s['eng'] = eng

            mat = inputNum(f"수학:{s['mat']}")
            if mat!=0: s['mat'] = mat

            # s['kor'] = inputNum(f"국어:{['kor']}")
            # s['eng'] = inputNum(f"영어:{['eng']}")
            # s['mat'] = inputNum(f"수학:{['mat']}")

