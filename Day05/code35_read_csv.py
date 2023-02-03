# Date : 2023-02-03
# Author : kimjihyeon-angela
# Desc : 공공데이터포털 csv파일 읽기
# 부산 광역시 시내버스, 마을버스 현황

import csv

# 파일 이름
fileName = 'busanbus.csv'
# 위치
dirName = 'C:/Source/StudyPython2023/'
fullPath = dirName + fileName

file = open(fullPath, 'r', encoding='utf-8')
# delimiter : 구분자
reader = csv.reader(file, delimiter=',')
next(reader)

for line in reader:
    print(line)
# 한줄씩, 리스트 형태로 출력됨
# 제목줄 없이 첫번째 줄부터 출력됨

file.close()