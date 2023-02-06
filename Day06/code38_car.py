# Date : 2023-02-06
# Author : kimjihyeon-angela
# Desc : 객체지향(상속)

# 차 부모 클래스
class Car:
    # Mother Class
    __name = '자동차'
    __color = 'white'
    __plate_number = ''
    __product_year = 1900
    # __사용했기 때문에 외부에서 함부로 못바꿈

    def __str__(self) -> str:
        return f'부모 클래스 입니다.'

    def get_name(self):
        return self.__name

    def run(self):
        return f'차가 달립니다.'

    def stop(self):
        return f'차가 멈춥니다.'


