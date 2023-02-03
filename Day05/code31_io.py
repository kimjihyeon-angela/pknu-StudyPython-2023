# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 입출력(Input, Output -> IO)
'''
number = input('수를 입력하세요 > ')
# 수를 입력하세요 입력 안해놓으면 아무것도 출력되는것 없이 커서가 깜박거림
# -> 무엇을 하라는 것인지 알 수 없음
# input을 만나면 무언가 입력하기 전에 종료되지 않음
number = int(number)
# => number를 int로 바꿔줘야 함 (number = int(number))
'''

# number = int(input('수를 입력하세요 > '))
# # 무조건 숫자만 받을 수 있도록 하는 방법

# print(number * 5)
# -> 모든 출력은 문자열로 됨 
# => 숫자를 넣어도 문자열로 인식하여 문자를 다섯번 출력함
print('Life' 'is' 'Short')
# LifeisShort로 출력됨
# ''안에서 띄어쓰기로 띄어쓰기 됨
# , 사용시 띄어쓰기됨

a = [1, 2, 3, 4]

for i in a:
    print(i)
# 한줄에 숫자 하나씩 나옴
    print(i, end=' ')
# 한줄에 숫자 4개 다 나옴