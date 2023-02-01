# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : 반복문 활용 별찍기


# 별 한줄에 하나씩 출력하기
for i in range(1,6):
    print('*')
print()


# 별 한개씩 늘려서 출력하기 1
star = ''
for i in range(1,6):
    star += '*'
    print(star)
print()


# 별 한개씩 늘려서 출력하기 2
# for i in range(1, 6)이랑 같은 의미임
for i in range(1, 6, 1):
    print('*' * i)
print()


# 별 한개씩 줄여서 출력하기
for i in range(5, 0, -1):
# 5부터 1까지 1씩 감소하면서 반복
    print('*' * i)