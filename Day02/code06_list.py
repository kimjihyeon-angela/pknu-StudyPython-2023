# Date : 2023-01-31
# Author : kimjihyeon-angela
# Desc : 복합형

# 리스트 
# 리스트 안쓰면 필요한 변수 개수만큼 변수를 만들어야함
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10

print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

# C에서는 리스트와 배열이 따로 있지만 파이썬에서는 리스트 == 배열임
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello',13,'World',True]
print(arr3)
print(type(arr3))
# <class 'list'>
print('arr1의 2번 인덱스 값 : ' + str(arr[2]))
# 3 출력됨
# print('arr1의 2번 인덱스 값 : ' + str(arr[3]))
# Index error

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

# 리스트 안에 리스트 넣기
arr6 = [1,2,3,4,[6,7,8,[9,10]]] 
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr7)


# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)
# tuple1.appen(4)
print(type(tuple1))
# <class 'tuple'> 결과값이 나옴

# 리스트는 배열에 값을 추가, 수정, 변경 할 수 있음 
# but 튜플은 한번 만든 배열에 값 변경할 수 없음


# 딕셔너리 (Hash, Hash Table 등 여러 명칭이 존재함 파이썬에서는 딕셔너리)
spiderman = {'name'   : 'Peter Parker',
             'age'    : 18, 
             'weapon' : 'web shooter'}
print(spiderman)
# {'name' : 'Peter Parker', 'age': '18', 'weapon': 'web shooter'}
# name : 키
# Peter Parker : 값
print(spiderman['weapon'])
# web shooter 결과가 나옴
# ctrl + space bar -> 원하는 명령어 -> tab
print(type(spiderman))
#<class 'dict'> 결과가 나옴


# 집합
set1 = set([1,2,3,4])
print(set1)
# {1, 2, 3, 4} 결과 나옴 -> 딕셔너리랑 같은 형태로 나옴
set1 = set("Hello World")
print(set1)
# {'o', 'e', 'W', 'H', ' ', 'l', 'r', 'd'} 
# => 중복된 값 하나로 합쳐져서 결과가 나옴