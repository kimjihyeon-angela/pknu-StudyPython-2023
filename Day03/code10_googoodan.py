# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : 구구단 프로그램

for x in range(2, 10):
    print(f'===== {x} 단 시작 =====')
    for y in range(1,10):
        print(f'{x} x {y} = {x * y:>2}', end = '  ')
        # :>2 => 2자리로 맞춰 오른쪽 정렬하는 방법
    print()
    print()
