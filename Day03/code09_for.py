# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : for 문

arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(item)
    sum += item
    #sum = sum + item
    

print('합계는',sum)


# 리스트를 편하게 만드는 방법
vals = [i for i in range(1,11)]
# 찾고자 하는 숫자 +1을 해야 함
# vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(vals)

#continue / break -> 반복문에서만 사용
num = 0
for item in vals :
    num += 1
    if num % 2 == 0:
        # continue
        # 이후의 것을 수행하지 않고 다시 for문으로 올라가는것
        # => 1 번 수는 1 입니다.
        #    3 번 수는 3 입니다.
        #    5 번 수는 5 입니다.
        #    7 번 수는 7 입니다.
        #    9 번 수는 9 입니다.
        break
        # break를 만나면 for문을 완전히 탈출
        # => 1번 수는 1 입니다. 의 결과만 나옴
    else:
        print(num, '번 수는', item,'입니다.')


print(range(0, 10)) # range(0, 10) => 0,1,2,3,4,5,6,7,8,9를 의미함
