# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 파일 읽어오기

file = open('./Day05/sample04.txt', 'r', encoding='utf-8')
'''
# 한줄(+ enter) 읽어오기
text = file.readline()
print(text)

# 한줄 읽어오기
text = file.read()
print(text)
'''

# 다 읽어오는 방법 : 반복문 사용
while True:
    text = file.read()

    if not text : 
        break
    
    print(text)

file.close()

# file open - close는 반드시 같이 해줘야함
# open, close는 무조건 같이 나와야 함 
