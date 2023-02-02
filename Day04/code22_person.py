# Date : 2023-02-02
# Author : kimjihyeon-angela
# Desc : 클래스 생성
# 객체 : 변수와 함수의 집합

class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # # 1. 초기화 추가 (원래소스에서 초기화부분이 추가됨을 의미함)
    # def __init__(self) -> None:     # class 생성하면 나타나는 함수(매직메서드) __을 찾을 수 있음 => 재정의(오버라이닝)해서 쓰는 것
    #     # (self) => class 내에서 함수 사용시 무조건 필요하기 때문에 자동으로 들어가짐
    #     # None 없어도 가능
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'
    #     # pass 없으면 error 발생함(초기에 뭐 할지 모르기 때문에 자동으로 입력되는 것임)
    #     # => pass 지우고 다른 내용 넣으면 error 없어짐

    # 2. 파라미터를 받는 생성자
    # def __init__(self, name, height, gender) -> None: # name, height, gender => 매개변수
    def __init__(self, name = '홍길동', height = 170, gender = 'male'): 
        self.name = name
        self.height = height
        self.gender = gender
        # 위에 있는 init도 쓰기 위해서는 파라미터에 기본값 지정해주면 됨
    
    def walk(self):
        print('걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            # run 함수 중 option == Fast경우가 참인경우 walk 함수를 실행한 후 빨리뜁니다! 실행함
            print(f'{self.name}이(가) 빨리 뜁니다!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    
    # 3. 생성자 외 매직 메서드(펑션)  __str__
    def __str__(self) -> str:  # 리턴값 : str => 문자열을 리턴해야 함
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'



jihyeon = Person() # 객체(object) 생성 => 실체(instance)가 만들어짐  
# 객체의 하나의 예이기 때문에 instance라고 부름
# class를 선언할 때는 () 사용 x 
# but, 밑에서 class를 사용할 때는 함수처럼 호출하는 것으로 () 사용 
jihyeon.name = '김지현'
jihyeon.height = '160'
jihyeon.gender = 'female'
jihyeon.blood_type = 'Rh+ AB'

print(f'{jihyeon.name}의 혈액형은 {jihyeon.blood_type}입니다.')
# if jihyeon.name 을 주석처리하면 홍길동의 혈액형은 Rh+ AB입니다. 결과가 나옴
# => blood_type은 Rh+ AB로 정보가 입력되었기 때문에 이름만 초기화로 넣은 홍길동이 나오고 혈액형은 새로 입력된 정보 출력됨

jihyeon.run('Fast')
# calss 내에 있는 함수 옵션에서 self가 빠질 경우 jihyeon.run('Fast')출력됨 
# run('') -> 천천히 뜁니다. 
# => if문의 옵션 조건이 참이 아니기 때문에 천천히 뜁니다.가 출력됨
# => if문의 옵션 조건에 거짓인 부분에 self.walk() 없기 때문에 걷습니다. 출력 x



# 1. 초기화 후 새로 객체 생성
hong = Person()
hong.run('')
# TypeError -> option에 대하 값을 넣지 않아 error 발생함
# hong.run('')
# 홍길동이(가) 천천히 뜁니다! 결과나옴
# __init__ 에서 초기화하며 name에 홍길동 입력했기 때문에 위 결과가 나옴


print('================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)


print('================')
# 3. 생성자 외 매직 메서드 __str__
print(ashely)
# class내 함수에서 __str__안 쓸 경우 error 발생함
print(hong)
print(jihyeon)

'''
단축키
break point -> 원하는 지점 클릭 후 f9
디버깅 끝내기 -> shift + f5
'''