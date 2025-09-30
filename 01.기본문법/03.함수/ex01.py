#함수정의
def grade(score):
    grade=""
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"        
    return grade
    #print(f"점수는 {score}, 학점:{grade}.")

while True:
    score = input("점수입력하세요 종료버튼은 0번>")
    if not score.isnumeric(): #숫자 말고 문자 입력시
        print("숫자로 입력하세요")
        continue
    if score=="0":
        print('프로그램을 종료합니다')
        break
    else:
        grade = grade(int(score))
        print(grade)