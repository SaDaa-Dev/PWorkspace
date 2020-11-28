# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화를 보러 갔을 때

# import theater_module as mv # 모듈에 별명 붙이기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price_morning, price
# price(5)
# price_morning(6)

# from theater_module import price_soldier as price
# price(5)


#여행사 패키지 사용
# import travel.thailand 
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# from travel import *
# # # trip_to = vietnam.VietnamPackage()
# # trip_to = thailand.ThailandPackage()
# # trip_to.detail()


# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


#패키지 설치 (pip)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장 함수 ( 이미 있는 함수들로써 라이브러리 설치를 하지 않아도 됨 )
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))
# name = "Jim"
# print(dir(name))


# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py 인 모든 파일


# os : 운영체제에서 기본으로 제공하는 기능
import os
# print(os.getcwd()) #현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다")
#     os.rmdir(folder)
#     print("폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)
