# Date : 2023-02-06
# Author : kimjihyeon-angela
# Desc : 객체지향(상속)

# Car 클래스를 상속한 제네시스 클래스

from code38_car import Car

# Child class
'''
부모 클래스에 있는 내용을 pass로 그대로 다 가져올 수 있음
부모 클래스에 없는 내용을 추가해서 사용할 수 있음
부모 클래스에 있는 내용을 재정의를 통해 새로 만들어서 사용할 수 있음
'''
class Genesis(Car):
    def __init__(self, name, color, 
                 plate_number, produc_year) -> None:
        super().__init__()
        # 부모클래스에서 가지고 있는 생성자 초기화
        # super : 부모 클래스에 있는 Car
        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = produc_year

        print(f'{self.__name}인스턴스 생성!')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self):
        return f'{self.__name}이(가) 달립니다.'

    def stop(self):
        return f'{self.__name}이(가) 멈춥니다.'

gv80 = Genesis('팔공이', 'black', '66오 1004', 2022)
# gv80.set_name('팔공이')
# set_name으로 부모 클래스에서 없는 함수를 새로 만듦
print(f'이 차의 이름은 {gv80.get_name()}입니다.')
# 부모의 클래스를 가져오면 부모 클래스에서 가지고 있던 이름을 그대로 가져옴
# => 새로 재정의 해줘야 이 차의 이름을 가지고 올 수 있음
print(gv80.run())
# 부모 클래스에서와 다르게 '재정의'함
# => 팔공이가 달립니다. 출력됨
print(gv80.stop())
# if child class에서 새롭게 정의하면 출력되는 내용이 바뀜
# child class에서 재정의하지 않으면 parent class에서 정의한 '차가 멈춥니다.' 출력됨
# child class에서 재정의한 경우 팔공이가 멈춥니다.로 바껴 출력됨