# Date : 2023-01-31
# Author : kimjihyeon-angela
# Desc : 자료형

# None : 값이 없는 값
None
# None은 아무것도 모르는 것을 의미함
print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val))
# <class 'int'>로 결과값이 나옴

val = 3.14
print(type(val))
# <class 'float'>로 결과값이 나옴

val = 'Hello'
print(type(val))
# <class 'str'>로 결과값이 나옴
# 같은 val이지만 쓸때마다 바뀜

val = 0b1010
print(type(val))
# 2진수를 표현하기 위한 키워드 0b
# 1010 = 10
# 2진수의 type도 int임 
# => <class 'int'>로 결과값 나옴

val = 15.458987545321654987651321654
print(type(val))

val = 4_520_000
print(val)
# 4520000으로 결과값 나옴

val = 3_099.99
print(val)
# 3099.99로 결과값 나옴

# 문자열
val = 'Life is short, You need Python.'
print(val)
print(type(val))

# 탈출문자 - \n, \t, \b
# \n : enter의 역할을 함
# \t : tap (스페이스4개 간격)
# \b : back space역할
val = 'Hell\nWorld'
print(val)

val = '''Life is short,
You need Python'''
print(val)

val = "Hi, I'm Jihyeon"
print(val)
val = 'Hi I\'m\'Jihyeon\''
print(val)
# 두개의 결과값이 같음 
# => 중간에 ' 넣어야 할 일 있으면 ""쓰고, 아니면 ''쓰기

# 불형 : 참 or 거짓
참 = True
거짓 = False

print(1 + 1 == 1)
# False
print(1 + 1 == 2)
# True
print(type(참))
# <class 'bool'>

print(거짓 == True)
# False
print(거짓 == False)
# True

print(거짓 is False)
# True

print(bool(1)) 
# 1 == True
print(bool(0)) 
# 0 == False
print(bool(2))
# 1이상은 True값이 나오지만 가능하면 1 or 0만 쓰기