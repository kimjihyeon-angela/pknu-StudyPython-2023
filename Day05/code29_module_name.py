# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 모듈 확인

print(f'code29_module_name : {__name__}')
# code29_module_name : __main__ 출력됨
# main : 엔트리 포인트(프로그램 시작 시 진입점)을 의미함

if __name__ == '__main__':
    print('name을 실행합니다!!') # code30에서 실행하면 여기 실행 안함
# if문 생략한 경우 code30에서 실행됨
# code 30에 가면 code 29는 __main__이 아니기 때문에 code30에서의 조건문 참에 해당하지 않게 됨
# 따라서 code29의 if문 안에서의 print 출력 안됨