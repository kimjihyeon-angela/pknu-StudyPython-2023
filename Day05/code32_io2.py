# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 다중입력

# x, y = input('두개의 영단어를 입력하세요 > ')
# print(x, y)
# 오류 발생함

# # if x로만 받으면 -> 두개의 단어가 x 하나의 단어로 받는 것임
# # 두개의 단어로 받기 위해서는 공백을 기준으로 잘라서 받을 수 있게 됨
# x, y = input('두개의 영단어를 입력하세요 > ').split()
# print(x)
# print(y)
# # 두개가 아닌 수의 단어를 입력하면 오류가 발생함
# # split 할 때 기준으로 자르기 때문에 쉼표를 기준으로 자르고 싶을 때 split(',')하면 됨


# 개수 제한 없이 입력 받을 수 있는 다중입력
inputs = list(map(str, input('단어를 입력해 주세요 > ').split()))
# map : 들어오는 값들을 나열해 주는 함수로 들어오는 값의 데이터형을 지정해줘야함
print(inputs)
# inputs = map(str, input('단어를 입력해주세요 >'))
# <map object at 0x000001FF747CAC50> 출력됨
# inputs = list(map(str, input('단어를 입력해주세요 >')))
# 글자 하나 하나, 공백까지 다 따로 출력됨
# inputs = list(map(str, input('단어를 입력해 주세요 > ').split()))
# 단어별로 구분해줌

# 숫자를 다중입력 받는 방법
inputs = list(map(int, input('정수를 입력해 주세요 > ').split()))
print(inputs)
# 문자가 들어올 경우 error 발생함