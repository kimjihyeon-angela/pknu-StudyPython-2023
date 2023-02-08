# %% [markdown]
# ## 웹 크롤링 (Web Crawling)
# 
# ### 인터넷 접속 라이브러리 추가
# 
# 

# %%
from urllib.request import urlopen, Request #(Day5에 한것과 같음)

# 도시별 날씨 검색 함수
def get_weather(city):
    # 기상청 홈페이지 도시별 날씨 페이지
    url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
    page = urlopen(url=url)

    text =  page.read().decode('utf-8')
    text = (text[text.find(f'>{city}</a>'):])

    # 기온 가져오기
    for i in range(7):
        text = text[text.find('<td>')+1:]

    start = 3
    # td>를 없애기 위해 start가 3이 되어야함
    end = text.find('</td>')
    # 뒤에 있는 </td>를 삭제해줌
    current_temp = text[start:end]
    # 7.1이 나올 수 있게 해줌

    print(f'{city}의 현재 기온은 {current_temp}˚C 입니다.')

    # 앞에서 7까지 가져온 뒤이기 때문에 뒤에 3개가 필요함 
    # 10번째에 있는 내용을 가져와야하지만
    # => for i in range(10)안됨

    # 습도 가져오기
    for i in range(3):
        text = text[text.find('<td>')+1:]

    start = 3
    end = text.find('</td>')
    current_humid = text[start:end]

    print(f'{city}의 현재 습도는 {current_humid}% 입니다.')

get_weather('부산')


