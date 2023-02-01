# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : 함수2

# 함수 만드는 방법 4가지
# 1. 파라미터 O  리턴 O
# 2. 파라미터 O  리턴 X
# 3. 파라미터 X  리턴 O
# 4. 파라미터 X  리턴 X

# 함수 정의
def add(x, y):
    result = x + y
    print(result)

def sub(x, y):
    result = x - y
    print(result)


def mul(x, y):
    result = x * y
    print(result)


def div(x, y):
    result = x // y
    print(result)


def hello():
    print('Hello~!!!')
    return

def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수 호출
hello()
print(hello2())

val = add(1024, 5)

val = sub(1024, 1000)

val = mul(512, 2)

val = div(108, 10)

# code 14랑 똑같은 결과가 나옴
# 값을 돌려주지 않아도 되는 return은 생략이 가능하기 때문에 print(result)다음에 return 생략된것임