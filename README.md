# StudyPython2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차
1. 기본
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. Python 기본
    - 콘솔출력
    - 주석

```python
# desc : 콘솔출력 - 주석
print('Hello, Python!!') # 콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자
```python
# 변수
val = 1


# 자료형
print(type(val))
# <class 'int'>


# 문자열 포맷팅
preword = 2
sayHello = 'Hey'
print(f"I'm so happy{preword} you,{sayHello}!!")
# f가 빠지면 {}가 그대로 출력됨
# f가 있으면 I'm so happy 2 you!! hey 출력됨

pi = 3.141592
print(f'파이는 {pi}입니다.')
# 파이는 3.141592입니다.
print(f'파이는 {pi:0.2f}입니다.')
# 파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.')
# 파이는      3.142입니다.
# => 앞자리를 10자리로 만듦
```

