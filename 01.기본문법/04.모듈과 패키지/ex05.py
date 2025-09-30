import os 

path = os.getcwd()
print('현재폴더', path)

check = path + "/04.모듈과 패키지/travel2"
if os.path.exists(check):
    # print('폴더가 존재합니다.')
    os.rmdir(check)
    print('폴더 삭제')
else:
    os.makedirs(check)
    print('폴더가 생성되었습니다.')