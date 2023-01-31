# Date : 2023-01-31
# Author : kimjihyeon-angela
# Desc : 변수

# val이라는 변수에 'Hello'넣고 출력
val = 'Hello'
print(val)

# val이라는 변수에 3.141592 넣고 출력
val = 3.141592
print(val)

# val이라는 변수에 10//2 넣고 출력
val = 10//2
print(val)

# => 파이썬에서는 변수에 문자, 숫자, 연산 다 들어감
# => 어떤 타입의 변수를 썼는지 잘 외우고 있어야 함 
# => 변수에 문자를 넣고 숫자와 연산 하면 안되기 때문

# 변수명은 주로 단어들의 조합을 함
plant_major_upper_code = 'U13TEMP'

# val과 plant_major_upper_code의 id 확인
print(id(val))
print(id(plant_major_upper_code))
# => 각자의 id가 다 존재함 
# => 두 변수의 주소가 다름