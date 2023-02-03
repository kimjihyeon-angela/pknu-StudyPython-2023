# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 파일 만들기

#file은 import 필요 x

# 파일을 새로 만들때는 무조건 파일모드 'w' 써야함
# 파일모드 'r' : 읽기 모드
# 파일모드 'a' : 추가 작성 모드 (처음 작성된 글 + 더 작성)


# 글자 인코딩
file = open('sample.txt', 'w', encoding='utf-8')
# 제대로 한글이 나오지 않음 
# 아스키코드로 표현되었기 때문 => 파일 열때 encoding을 Unicode(utf-8)로 바꿔줘야 함
# why? 한글단위 기준 : 2바이트, 미국(영어)기준(1바이트) 
# ASCII -> 한단어를 표현하는 체계(영어)
# UNI CODE (UTF-8)-> 모든 나라 언어를 다 표현 가능 

file.write('안녕하세요~\n')
# \n -> new line
file.write('첫번째 파일입니다.\n')

file.close()
# 왼쪽 탐색기에 sample.txt 생성됨
# but 현재 내용 아무것도 없음 
# why? -> 안에 아무 내용 안썼기 때문 
# 내용 적는 법 : open 과 close 사이에서 file.write('') 해주기

# 이렇게 실행하면 터미널에 아무말도 나타나지 않음 => print 해주기
print('sample01.txt가 생성되었습니다.')



# 파일/ 폴더 경로
'''
절대 경로
- c:\Source\StudyPython2023 => 경로를 다 적어주는 것
- 처음부터 끝까지 다 적는것
- \ 하나만 쓰기, \\ 2개 쓰기, / 쓰기 3가지 방법이 있음

\ : 특수기호로 한번만 쓴 경우 잘 못알아들을 수 있음 => 2개 써주기

상대경로
- 나의 위치에서 부모, 형제만 보는 것
- . : 본인
- .. : 부모
'''

# 절대경로에 파일 생성하는 방법 1
file = open('C:\\DEV\\Temp\\Bank\\sample01.txt', 'w', encoding='utf-8')
file.write('안녕하세요~\n')
# \n -> new line
file.write('두번째 파일입니다.\n')
file.write('절대 경로에 파일이 생성될겁니다.\n')
file.close()
print('sample01.txt가 생성되었습니다.')


# 절대경로에 파일 생성하는 방법 2
file = open(f'C:\DEV\Temp\Bank\sample02.txt', 'w', encoding='utf-8')
file.write('안녕하세요~\n')
# \n -> new line
file.write('세번째 파일입니다.\n')
file.write('절대 경로에 파일이 생성될겁니다.\n')
file.close()
print('sample02.txt가 생성되었습니다.')


# 절대경로에 파일 생성하는 방법 3
file = open('C:/DEV/Temp/Bank/sample03.txt', 'w', encoding='utf-8')
file.write('안녕하세요~\n')
# \n -> new line
file.write('네번째 파일입니다.\n')
file.write('절대 경로에 파일이 생성될겁니다.\n')
file.close()
print('sample03.txt가 생성되었습니다.')


# 상대경로에 파일 생성하는 방법 (본인폴더에서 형제인 Day05에 지정)
file = open('./Day05/sample04.txt','w', encoding='utf-8')
file.write('안녕하세요~\n')
file.write('상대 경로에 파일이 생성될겁니다.\n')
file.close()
print('sample04.txt가 생성되었습니다.')

# 상대경로에 파일 생성하는 방법 (본인폴더에서 부모폴더에서 형제폴더인 Day04에 지정)
file = open('./Day05/../Day04/sample05.txt','w', encoding='utf-8')
file.write('안녕하세요~\n')
file.write('상대 경로에 파일이 생성될겁니다.\n')
file.close()
print('sample05.txt가 생성되었습니다.')

# 상대경로에 파일 생성하는 방법 (본인폴더에서 부모폴더인 Source폴더에 지정)
file = open('../sample06.txt','w', encoding='utf-8')
file.write('안녕하세요~\n')
file.write('상대 경로에 파일이 생성될겁니다.\n')
file.close()
print('sample06.txt가 생성되었습니다.')