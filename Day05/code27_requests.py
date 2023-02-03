# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 외부 패키지 사용

import requests
# pip install requests 안하면 requests 찾을 수 없음

res = requests.get('https://www.naver.com')
print(res.status_code)
# urllib에서 print한 코드와 같은 200 출력됨

print('=========================')
print(res.content)
# html 코드 출력됨
# 터미널에서 다 안나옴(축소시켜짐)

