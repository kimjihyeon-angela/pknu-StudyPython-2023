# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : random 모듈사용

import random

# print(random.choice(range(1,7)))
# 1~6까지의 숫자 중 랜덤하게 숫자 한 개 프린트 됨

# 1 부터 45까지의 리스트(배열) 만들기
numbers = [i for i in range(1,46)]

# 로또 번호 들어갈 lottery 리스트 만들기
lottery = []

# 6개의 i를 받을 수 있도록 for문 만들기
# i의 범위 : 0~5 => 6개
for i in range(6):
    lottery.append(random.choices(numbers))
    # [[5], [16], [27], [32], [16], [33]]
    lottery.append(random.choice(numbers))
    # [5, 22, 43, 24, 21, 6]
    # choice와 choices의 결과가 조금 다름

# 로또 번호 출력하기
print(lottery)
# 중복된 숫자가 나올 수 있음