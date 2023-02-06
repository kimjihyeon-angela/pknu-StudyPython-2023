# Date : 2023-02-06
# Author : kimjihyeon-angela
# Desc : 콘솔 출력 보충

# 이스케이프 캐릭터 (탈출문자)

'''
\r, \n(new line), \t(tab), \b(back space), \'('), \"("), \\, \f, \0(널문자)
예전에는 \r\n으로 사용했었지만 지금 윈도우에서는 \n으로 통합(?)됨
'''

print('1. Hello.\r\nWorld')
print('2. Hello.\nWorld')
# 탈출문자 2개 쓸 필요 없음  => \n 쓰기
print('3. Hello.\n\tWorld')
print('4. Hello.\n\t\bWorld')
print('5. Hello.\n\t\b\'World\'')
print('6. Hello.\n\t\b\"World\"')
print('7. Hello.\n\t\b"World"')
# 6번과 7번 출력되는 것은 같음
# => 밖에서 ''로 감싸고 있기 때문에 ""는 그냥 써도 상관 없음
print('8. Hello.\n\t\b\\World')
print('9. Hello.\n\t\b\World')
# 8번 9번 출력되는 것 같음
# 파이썬에서는 \한번만 써도 가능 (다른 언어에서는 불가)
print('10. Hello\0')


# 문자열 포맷팅
# %로 포맷코드를 시작
me = '저'
name = '김지현'
age = 20
print('%s는 %s입니다. %d대입니다.'%(me, name, age))
print(f'{254.112233:.2f}') # 254.11출력됨 => 소수점 2자리에서 자름
print('%4.4f'%254.112233) # 254.1122로 출력됨 앞에 4 : 전체 길이(점 포함), 뒤에 4 : 소수점 뒤 
print('%9.4f'%254.112233)
print('%9.2f'%254.112233)