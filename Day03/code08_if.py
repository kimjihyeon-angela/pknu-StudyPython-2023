# Date : 2023-02-01
# Author : kimjihyeon-angela
# Desc : if문

name = '지현'      
state = '안아픔'
# 변수에는 값을 넣는 것이기 때문에 = 1개 필요
# if문안에서는 값을 비교하는 것이기 때문에 == 2개 필요
# 비교 연산자 -> == : 같음 / != : 다름 을 의미함

if name == '지현':
    print('진료실에서 담당의사를 만납니다.')
    if state == '아픔':
        print('선생님, 배가 아파요')
        print('어디가 어떻게 아프십니까?')
    else :
        print('어디가 아프십니까?')
        print('안아픈데요')
        print('그럼, 왜오셨어요?')
elif name == '다원': # else if -> elif
    print('주사실로 갑니다.')
    print('바지 내리세요')
else :
    print('조용히 기다립니다.')

# if 문이 끝이라는 것을 알리기 위해 콜론(:) 필요
# 들여쓰기 중요함
# 중복 if문 -> if문 안에 if문 넣기 가능