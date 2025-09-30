#1 남탕: 남자이거나 여자면서 4세 미만.
#2 여탕: 여자이거나 남자면서 4세 미만.
while True:
    type = input("1.남탕|2.여탕|0.종료>")
    if type == "0":
        print("프로그램을 종료합니다.")
        break

    elif type == "1" or type =="2" :
        gender = input("1.남자|2.여자>")
        if type == "1": #남탕
            if gender == "1": #남자
                print("남자이므로 남탕 입장이 가능합니다.")
            else: #여자
                age = int(input("나이>"))
                if age < 4: #4세 미만 여자
                    print("여자지만 4세 미만이므로 남탕 입장 가능합니다")
                else: 
                    print("4세 이상 여자는 남탕 입장 불가.")

        if type == "2": #여탕
            if gender == "2": #여자
                print("여자이므로 여탕 입장이 가능합니다.")
            else:
                age = int(input("나이>"))
                if age < 4: #4세 미만 남자
                    print("남자지만 4세 미만이므로 여탕 입장 가능합니다")
                else: 
                    print("4세 이상 남자는 입장 불가.")
        

    else: 
        print("0~2 숫자를 입력하세요.")
