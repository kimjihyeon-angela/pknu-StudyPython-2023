# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : urllib 패키지 불러오기

from urllib.request import Request, urlopen
# request(요청) - response(응답)
# urllib.requst 중에서 Requst, urlopen을 사용하겠다는 의미

req = Request('https://www.naver.com')
# Request : Class
# Request() => 생성자로 req 객체 만듦
# crtl 누르고 위 링크 누르면 해당 링크로 연결됨
# 인터넷 : 네트워크를 통한 request와 response임

res = urlopen(req)
# urlopen => 함수
print(res.status)
# 200 출력됨 -> http의 코드임 => 웹사이트에 정상적으로 접근했다는 의미
# if 404 나오면 페이지를 찾지 못했다는 의미임

