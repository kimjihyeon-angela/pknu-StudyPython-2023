# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : 함수

# 함수 정의 (실행x)
def add(x, y):
    result = x + y
    return result
# 이 상태로 실행 -> 아무일도 일어나지 않음 => just 정의이기 때문
# 함수를 불러야 사용할 수 있게 됨


def sub(x, y):
    result = x - y
    return result


def mul(x, y):
    result = x * y
    return result


def div(x, y):
    result = x // y
    return result

# 함수 호출
val = add(1024, 5)
print(val)
# => 값을 받기 위해서 함수 정의에서 return을 받아야 함
# => 함수 정의에서 def add(x,y):
#                      result = x + y 만 했을 경우 None 출력됨


val = sub(1024, 1000)
print (val)

val = mul(512, 2)
print (val)

val = div(108, 10)
print (val)