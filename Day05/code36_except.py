# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 예외처리(exception handling)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    x,y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
# 이렇게만 하면 밑으로 내려가서 진행됨
# 입력에 실패하면 프로그램 종료해야함 종료할 수 있는 함수 입력
    exit()
# exit구문 뒤에 finally 입력한 경우 finally의 함수를 수행한 후 exit 수행함

# 예외처리방법 1(원시적인 방법)
# 이렇게 되면 더하기, 곱하기도 하지 않고 프로그램 종료됨
# if y == 0:
#     print('y에 0을 넣지 마세요')
    # exit()

print('테스트 시작')
# try except 문으로 예외처리하기
try:
    print(div(x,y))
# ZeroDivisionError 발생 시 아래 문장이 출력됨
# 굳이 except ZeroDivisionError 작성할 필요 없이 우선 Exception만 하기
except ZeroDivisionError as e:
    print('0으로 나누면 안됩니다.')
# ZeroDivisionError 의 부모 에러로 Exception은 가장 마지막에 있어야함
# 다른 에러를 처리할 때도 마찬가지임
except Exception as e:
    print(e)
# Exception 클래스 사용시 어떤 에러가 발생했는지 알려줌
finally:
    print('계산은 계속됩니다!')
# finally는 예외가 발생해도 안해도 출력됨
# 무조건 출력해야하는 경우 finally에 입력

print(add(x,y))
print(mul(x,y))
# y에 0을 넣으면 0으로 나누기가 안되기 때문에 error가 발생함
# 프로그램이 비정상적으로 종료되는 예외상황임
# 다른 숫자들은 제대로 작동하기 때문

'''
0으로 나눌 경우
  File "c:\Source\StudyPython2023\Day05\code36_except.py", line 18, in <module>
    print(div(x,y))
          ^^^^^^^^
  File "c:\Source\StudyPython2023\Day05\code36_except.py", line 12, in div
    return a / b
           ~~^~~
이런 error 발생
=> 18line 과 12line 두개 다 확인해야함
=> 디버깅 해봐야 함
-> 디버깅 시 오류난 포인트 윗줄 break point 걸기
'''