# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : 라이프 스코프

a = 1

'''
def vartest(a):
    a = a + 1
    return a
'''
# def vartest(a): 를 하고 global a를 입력할 경우 어떤 a를 이용하는 것인지 알 수 없기 때문에 error 발생

def vartest():
    global a
    # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다는 의미
    a = a + 1
    return a


a = vartest(a)
print(a)