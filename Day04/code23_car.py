# Date : 2023-02-02
# Author : kimjihyeon-angela
# Desc : 클래스 생성2

# 자동차 클래스
class Car:
    __number = '132구 5678'

    # 차 번호 넘겨 받기
    def get_number(self) -> str:
        return self.__number

    # 클래스 외부에선 변경x, 멤버함수로는 내부 조작 가능
    def set_number(self, number):
        self.__number = number
    
    # 초기화
    # def __init__(self) -> None:
    #     print('__init__')

    # 차 번호 수정할 수 있도록 초기화 하는 방법
    def __init__(self, number = '132구 5678') -> None:
        print('__init__')
        self.__number = number
        

    # 클래스를 만드는 작업이라고 볼 수 있음(문법적으로 존재 but, 잘 안씀,,)
    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls)
        # super(녹색) -> class 
        # super => Car class의 부모 class

    def __str__(self) -> str:
        return f'차 번호는 {self.__number}입니다.'
    
mycar = Car()
# new -> init 순서로 매직매서드가 진행됨 (str -> 생성될때 시작되는 것이 아니라 print 할때 시작됨)
print(mycar)
# prtint를 해야 str 됨
# __str__에서 입력한 대로 차 번호는 ~~ 입니다. 출력됨
print(mycar.get_number())
# 차 번호만 나옴

# 차 번호 바꾸기를 못하게 한 경우(__사용, 인캡슐라이션..?) -> 차 번호 바꿀 수 없음
mycar.__number = '54라 9538'
print(mycar.get_number())
print(mycar)

# if 차 번호 바꾸게 하려면 init에서 설정할 수 있음
yourcar = Car('88호 1234')
print(yourcar)
# 처음 실행할 때 차 번호 변경할 수 있지만 만들고 나서는 차 번호 수정 불가
# 외부에서는 멤버변수에 접근 불가
yourcar.__number = '54라 9999'
print(yourcar)
print('========')
# 클래스 내부함수 활용하여 번호 바꾸기 가능
yourcar.set_number('55구 5959')
print(yourcar)