# Date : 2023-01-31
# Author : kimjihyeon-angela
# Desc : 연산자

# 할당연산 assignment
# 2 = 1 (x)
# 1 = val (x)
val = 1
# 왼쪽은 무조건 변수가 되어야 함, 값이 와서는 안됨


# equal 연산자
print(1 == 1)
# True 결과 나옴


# 사칙 연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2)
print(1024 // 2)
print(1 / 3)  # 소수 나누기 => 0.333333333333
print(1 // 3) # 정수 나누기 => 0
print(1 % 3)  # 나머지      => 1

# print(6 / 0)
# print(6 // 0)
# 0으로 나누기 불가능함

print (2 ** 10) # 2의 10승


# 문자열 연산
first = 'Hello'
second = 'World'
print(first + second)
# HelloWorld출력됨
print(first + ' ' + second)
print(first,second)
# 2개의 결과는 같게 나옴 => Helo World
print(first * 4)
# HelloHelloHelloHell => first를 4번 출력해줌
# print(first - seconde)
# print(first / second)
# 문자열 연산 : +, *만 가능


# 문자열 길이
print(len(first))
# 5출력됨 => Hello의 길이를 출력하는 것이기 때문
print(first[0]) # H
print(first[1]) # e
print(first[2]) # l
print(first[3]) # l
print(first[4]) # o
# print(first[5]) - (Index error)나옴

print(first[-1]) # o
print(first[-2]) # l
print(first[-3]) # l
print(first[-4]) # e
print(first[-5]) # H
# 뒤에서부터 인덱스 찾아나감
# print(first[-6]) # Index error 


# 리스트 자르기(스플릿)
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
# print(current[0:3]) # 3Index 앞까지 잘라주기 때문에 202가 나옴
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[-19:-15])  # 2023


# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)  # [7,2,3,4,5]

# que[5] = 10
# print(que)
# Index Error -> 최고 Index는 4이기 때문에 que[5]에 값 입력 안됨

que.append(10)
print(que)
# que에 값을 추가하기 위해 .append(값) 입력해야함
# []인덱스 번호로는 값 추가하기 불가능

que.insert(3, 99)
print(que)
# 3번 인덱스 값에 99 넣기 => 4가 99로 바뀜

que.remove(99)
print(que)
# [7, 2, 3, 4, 5, 10] 결과 출력됨

# append : 뒤에 값 추가
# insert : 내가 원하는 위치의 값 변경 
# remove : 내가 원하는(해당) 값 삭제

# tup = (1, 2, 3, 4, 5)
# tup[1] = 9
# print(tup) # 튜플은 값 수정, 추가, 변경이 불가능 하기 때문에 오류(type error)가 발생함


# 문자열 == 문자 리스트
title = 'python'

print(title[0])

# title[0] = 'P'
# print(title[0])
# python 똑같이 나옴
# => 문자열에서는 값 변경이 안됨
print('P' + title[1:])
# => Python 출력됨


# 일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)
# 값 변경 가능


# 문자열 포맷팅
print("I'm so happy {0} you!!".format(2))
# I'm so happy 2 you!!
# {인덱스 번호} .format(들어가야 할 값)
# if) "I'm so happy {0} you!! {1}".format(2, 'hey')
# => I'm so happy 2 you!! hey

preword = 2
sayHello = 'Hey'
print(f"I'm so happy{preword} you,{sayHello}!!")
# f가 빠지면 {}가 그대로 출력됨
# f가 있으면 I'm so happy 2 you!! hey 출력됨

pi = 3.141592
print(f'파이는 {pi}입니다.')
# 파이는 3.141592입니다.
print(f'파이는 {pi:0.2f}입니다.')
# 파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.')
# 파이는      3.142입니다.
# => 앞자리를 10자리로 만듦


# 문자열을 특정 문자로 자르기
full_name = 'Kim. Ji Hyeon'
vals = full_name.split()
# split => 자르기 => 기준 : ' ' (스페이스)
print(type(vals))
# <class 'list'>

vals = full_name.split('.')
# split 기준 : '.'
print(vals)
# ['Kim', 'Ji Hyeon']


# 문자열 특정 문자로 바꾸기
print(full_name.replace('Kim.', 'Angela'))
# Kim. 을 Angela로 바꾸기


# 문자열 공백 없애기
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|')
# 왼쪽 공백 없애기
#Hello~ Bye~          |
print(hi.rstrip() + '|')
# 오른쪽 공백 없애기
#          Hello~ Bye~|
print(hi.strip() + '|')
# 오른쪽, 왼쪽 공백 없애기
# Hello~ Bye~|

print(full_name.index('H'))
# print(full_name.index('G'))
# G를 발견하기 못하는 경우 error 발생함
print(full_name.find('G'))
# -1값 나옴 
# => index 보다 find 쓰기


# 찾는 단어의 개수
print(full_name.count('i'))


# 모든 단어를 대문자, 소문자로 변경
print(full_name.upper())
print(full_name.lower())


# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)