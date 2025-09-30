import os , pandas as pd
file_prof = '학사관리/교수.csv'

def inputNum(title):
    while True:
        num = input(title)
        if num =='':
            return ''
        elif num.isnumeric():
            return int(num)
        else:
            print('숫자로 입력하시오')

def prof_list():
    prof = pd.read_csv(file_prof, index_col='교수번호')
    for idx, row in prof.iterrows():
        print(idx, row['교수이름'], row['교수학과'], row['임용일'], end=' ')
        print(f'{row["급여"]:,}')

def prof_search(code):
    prof = pd.read_csv('학사관리/교수.csv' , index_col='교수번호')
    stu = pd.read_csv('학사관리/학생.csv', index_col='학생번호')
    cou = pd.read_csv('학사관리/강좌.csv', index_col='강좌번호')
    
    if not code in stu.index:
        print('해당 학번이 존재하지 않음')
        return
    
    if code in prof.index:
        prof_row = prof.loc[code]
        print(code, prof_row['교수이름'], prof_row['교수학과'])

        print('담당학생-----------------------------')
        filt = stu['지도교수'] == code
        stu_rows = stu[filt]
        for idx, row in stu_rows.iterrows():
            print(idx, row['학생이름'], row['학생학과'])

        print('담당강좌-------------------------------')
        filt = cou['담당교수'] == code
        cou_rows = cou[filt]
        for idx, row in cou_rows.iterrows():
            print(idx, row['강좌이름'], row['강의시수'])
    else:
        print('해당 교수 없음')

def stu_list():
    stu = pd.read_csv('학사관리/학생.csv')
    prof = pd.read_csv('학사관리/교수.csv')
    merge = stu.merge(prof, left_on='지도교수', right_on='교수번호')
    merge = merge.sort_values('학생이름')
    for idx, row in merge.iterrows():
        print(row['학생번호'], row['학생이름'], row['학생학과'], row['교수이름'], end=' ')
        print(row['생년월일'], row['학년'])

def stu_search(code):
    stu = pd.read_csv('학사관리/학생.csv', index_col='학생번호')
    prof = pd.read_csv('학사관리/교수.csv', index_col='교수번호')
    enroll = pd.read_csv('학사관리/수강.csv', index_col=['학생번호', '강좌번호'])
    enroll.fillna(0, inplace = True)
    cou = pd.read_csv('학사관리/강좌.csv', index_col='강좌번호')

    if not code in stu.index:
        print('해당 학번이 존재하지 않음')
        return
    
    stu_row = stu.loc[code]

    advisor = stu_row['지도교수']
    prof_row = prof.loc[advisor]
    print(stu_row['학생이름'], stu_row['학생학과'], prof_row['교수이름'])

    print('\n수강과목')
    print('-' * 50)
    enroll_rows = enroll.loc[code]

    sum = 0 

    for idx, row in enroll_rows.iterrows():
        cou_row = cou.loc[idx]
        print(idx, cou_row['강좌이름'], row['신청일'], row['점수'])
        sum += row['점수']
    avg = sum/len(enroll_rows)
    print(f'평균:{avg:.2f}')


def cou_list():
    cou = pd.read_csv('학사관리/강좌.csv')
    prof = pd.read_csv('학사관리/교수.csv')
    merge = cou.merge(prof, left_on='담당교수', right_on='교수번호')
    merge = merge.sort_values('강좌이름')
    for idx, row in merge.iterrows():
        print(idx + 1 , row['강좌번호'], row['강좌이름'], row['강의실'], row['교수이름'], end=' ')
        print(row['강의시수'], row['최대인원'])

def cou_search(code):
    stu = pd.read_csv('학사관리/학생.csv', index_col='학생번호')
    prof = pd.read_csv('학사관리/교수.csv', index_col='교수번호')
    enroll = pd.read_csv('학사관리/수강.csv', index_col=['강좌번호', '학생번호'])
    enroll.fillna(0, inplace = True)
    cou = pd.read_csv('학사관리/강좌.csv', index_col='강좌번호')

    if not code in cou.index:
        print('해당 강좌가 존재하지 않음')
        return
    
    cou_row = cou.loc[code]

    advisor = cou_row['담당교수']
    prof_row = prof.loc[advisor]
    print(cou_row['강좌이름'], cou_row['강의실'], prof_row['교수이름'])

    print('\n수강학생')
    print('-' * 50)
    enroll_rows = enroll.loc[code]

    sum = 0 

    for idx, row in enroll_rows.iterrows():
        stu_row = stu.loc[idx]
        print(idx, stu_row['학생이름'], row['신청일'], row['점수'])
        sum += row['점수']
    avg = sum/len(enroll_rows)
    print(f'평균:{avg:.2f}')

while True:
    os.system('cls')
    print('-' * 50)
    print('학사관리')
    print('-' * 50)
    print('[1]교수목록')
    print('[2]교수검색')
    print('[3]학생목록')
    print('[4]학생검색')
    print('[5]강좌목록')
    print('[6]강좌검색')
    print('[0]종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu == '0':
        print('프로그램 종료')
        break
    elif menu == '1':
        prof_list()
        input('아무키나 누르시오')
    elif menu == '2':
        while True:
            code = inputNum('교수번호>')
            if code =='':break
            prof_search(code)
    elif menu == '3':
        stu_list()
        input('아무키나 누르시오')
    elif menu == '4':
        while True:
            code = inputNum('학생번호>')
            if code =='':break
            stu_search(code)
    elif menu == '5':
        cou_list()
        input('아무키나 누르시오')
    elif menu == '6':
        while True:
            code = input('강좌번호>')
            if code =='':break
            cou_search(code.upper())

