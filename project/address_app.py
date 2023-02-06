# Date : 2023-02-06
# Author : kimjihyeon-angela
# Desc : 주소록 앱

# 15. 예외처리
# 15-1. 파일 없을 때 나는 예외 => 파일을 새로 만들며서 예외 처리
# 15-2. 메뉴 번호 입력 숫자 외 다른거 입력했을 때 나는 예외 => 다른거를 다 0으로 처리
# 15-3. 입력시 / 개수 다를때 나는 예외 => 제대로 입력해달라는 메세지 출력

import os #운영체제 모듈 불러오기

class Contact:
# 2. 생성자 - 이름, 전화번호, 이메일, 주소 받을 예정
    # 여러개의 변수를 받아야 하기 때문에 init 해줌
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num    
        self.__email = email
        self.__addr = addr

    
# 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이    름 : {self.__name}\n'
                   f'핸 드 폰 : {self.__phone_num}\n'
                   f'이 메 일 : {self.__email}\n'
                   f'주    소 : {self.__addr}')
        return str_res


# 10. 객체 존재여부 확인 (클래스 함수)
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False

    
# 11. 각 멤버변수 접근할 수 있는 함수(getset)
    # getname, getphonenum, getemail, getaddr
    def getName(self) -> str:
        return self.__name

    def getPhoneNum(self) -> str:
        return self.__phone_num

    def getEmail(self) -> str:
        return self.__email

    def getAddr(self) -> str:
        return self.__addr


# 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr = input('정보 입력(이름/ 전화번호/ 이메일/ 주소) > ').split('/') 
    # print(name, phone_num, email, addr)
    # 7. Contact 객체 만들기
    contact = Contact(name, phone_num, email, addr)
    return contact


# 9. 주소록 출력
def get_contacts(list):
    for item in list:
        print(item)
        print('====================')


# 10. 주소록 삭제
def del_contact(list, name):
    count = 0
    for i, item in enumerate(list):
    # enumerate : 리스트에 있는 내용들의 번호를 찾아낼 수 있음
    # enumerate : 리스트의 인덱스 추가 생성
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제
    # 11. 삭제 시 멘트 출력
    if count > 0:
        print('삭제되었습니다.')
    else :
        print('삭제할 주소록이 없습니다.')

# 13. 주소록 파일 저장
def save_contacts(list):
    file = open('C:/Source/StudyPython2023/project/contacts.txt',
                'w', encoding='utf-8')
    
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')

    file.close


# 14. 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/Source/StudyPython2023/project/contacts.txt',
                    'r', encoding='utf-8')
    except Exception as e:
        # print('contacts.txt 파일이 없습니다.')   
        # print('파일을 생성하고 다시 실행하세요.')
        # exit()
        # 파일이 없어 생기는 예외 -> 파일생성하고 함수 탈출
        # 파일이 없어 새로 파일을 만들어 냄
        f = open('C:/Source/StudyPython2023/project/contacts.txt',
                 'w', encoding='utf-8')
        f.close
        return

    while True:
        line = file.readline().replace('\n','') #15. 문장 끝 \n 제거
        if not line:
            break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close


# 추가. 화면 클리어를 위한 함수 (주소록에 들어가는 로직x)
def clear_console():
    command = 'clear' # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'):
        #in : nt, dos(윈도우 운영체제)라면
        command = 'cls'
        # cls : 윈도우 화면 클리어 명령어 
    os.system(command)


# 6. 메뉴 표시
def get_menu():
    str_menu = ('주소록 앱 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱 종료\n')
    print(str_menu)
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e: # 15-3 숫자 외 입력했을 때 발생하는 예외 처리
        menu = 0
        # 영문자, 특수문자 -> 전부 0으로 처리
    return menu



# 3. 전체 실행
def run():
    contacts = list() # 주소를 담기 위한 빈 리스트 생성
    load_contacts(contacts) # 14. 주소록 읽어오기
    # temp = Contact('김지현','010-1234-5678',
    #                'angela9830@naver.com', '경남 양산시 ...')
    # set_contact()
    clear_console()
    while True:
        sel_menu = get_menu()
        # 8. 연락처 추가
        if sel_menu == 1: # 8. 연락처 추가
            # clear_console()
            try: # 15-3 연락처 입력 잘못했을 때 예외처리
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공') # 아무것도 안받는 입력
            except Exception as e:
                print('이름/전화번호/이메일/주소 순으로 똑바로 입력해주세요.')
                input()
            finally:
                clear_console()

        elif sel_menu == 2: # 9. 연락처 출력
            # clear_console()
            get_contacts(contacts)
            input('주소록 출력 완료')
            clear_console()

        elif sel_menu == 3: # 10. 연락처 삭제
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()

        elif sel_menu == 4: # 13. 앱종료시 주소록 파일에 저장
            save_contacts(contacts)            
            break

        else:
            clear_console()


# 1. 메인 실행 영역 
if __name__ == '__main__':
    # print('주소록 앱 시작합니다.')
    run()