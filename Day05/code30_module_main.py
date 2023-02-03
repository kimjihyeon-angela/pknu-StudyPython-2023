# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 모듈확인2

import code29_module_name

print(f'code30_module_main : {__name__}')
# code30_module_main : __main__ 출력됨
# if code29_module_name을 import한 경우 
# => code29_module_name : code29_module_name => 불러만 오기 때문에 main이 아님
#    code30_module_main : __main__
# 엔트리 포인트(main)는 하나만 있음 -> 실행하는 애만 main
# => 부르는 애 이름은 이름이 됨 (code29_module_name) 

# C -> int main(void)와 동일
if __name__ == '__main__':
    print('main을 실행합니다!!')
