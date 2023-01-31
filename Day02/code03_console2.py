# Date : 2023-01-31
# Author : kimjihyeon-angela
# desc : 콘솔 출력
# 엔터를 공백으로 변경

print('*', end=' ')
# print의 마지막은 enter -> end = ' '마지막을 공백으로 넣겠다는 의미로 * ** 이렇게 출력됨
print('**', end=' ')
print('***', end=' ')
print('****', end=' ')
print('*****')
#  => 한줄에 다 넣고 싶을 경우 print의 옵션으로 end 하나 더 넣어줘야함
# f12 누르면 도움말 나옴


# 공백 구분자를 /로 변경
print('a', 'b', 'c')
# a b c로 결과가 나옴
print('a', 'b', 'c', sep='/')
# a/b/c로 결과가 나옴 
# => 공백 구분자를 /로 바꾼 것임