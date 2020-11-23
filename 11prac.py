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

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()