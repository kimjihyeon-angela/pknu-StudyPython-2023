# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : 라이프 스코프2

# 전역/ 지역 변수

num = 1

for i in range(1, 11):
    num = i * num
    print(f'{i +1}번')

    if i % 3 == 0:
        res = '테스트'
        print(res)


print(f'결과 {num}')
print(res)