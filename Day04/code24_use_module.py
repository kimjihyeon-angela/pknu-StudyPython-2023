# Date : 2023-02-02
# Author : kimjihyeon-angela
# Desc : 모듈 사용

import math
# import math as m => math를 m으로 바꿔줘야함 
# => math라는 모듈을 m이라고 바꿔서 동작시킴
# 모듈 -> 모두 class화 되어 있는 것 x
# class로 안된 모듈 => math

import code22_person as p
# 우리가 만든 클래스
from code23_car import Car

print(math.pi)

print(math.sin(0))
print(math.cos(0))
print(math.tan(0))
print(math.ceil(3.2))  # 올림
print(2**10)
print(math.pow(2, 10)) # 2의 10승 (2**10과 같음)
# 2**10과 차이점 : 정수, 소수로 출력됨

# 우리가 만든 모듈 사용
me = p.Person('홍길순', 155, '여성')
print(me)


mycar = Car()
print(mycar)