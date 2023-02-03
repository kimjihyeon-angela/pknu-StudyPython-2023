# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : Day03에 만든 계산기 모듈 사용

from code17_calculator import *
# *은 all(전부)를 의미함
# code17_calculator 내에 있는 함수 중 한개만 사용하고 싶을 때 from과 import를 사용
# from을 사용하면 code17_calculator 내에 있는 함수 중 import를 통해 골라서 사용 가능
# code17_calculator 내에 있는 함수 전부 다 사용하고 싶은 경우 * 사용

print(calc('add', 5, 7, 17))
# code17_calculator에 있는 모든 결과물 다 출력되고 print도 나옴
# => 모듈을 만들때는 프린트를 작성하지 않음 
# => 모듈에서 프린트 작성된 부분까지 출력되어 나오기 때문