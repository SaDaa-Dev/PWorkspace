# 리스트 []

# # 지하철 칸별로 10명, 20명 , 30명
# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호는 몇 번째 칸에 있는가?
# print(subway.index("조세호"))

# # 하하가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈을 유재석 / 조세호 사이에 태움
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # 정렬 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용 가능
# num_list = [5,4,3,2,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전 ------------------------------------------------------
# cabinet = {3:"유재석", 100:"김태호"} # key 3 데이터는 유재석
# print(cabinet[3]) 
# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))

# print(3 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"} 
# print(cabinet["A-3"])

# #새 손님
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]

# #key들만 출력
# print(cabinet.keys())

# #key, value 쌍으로 출력
# print(cabinet.items())

# # 폐점
# cabinet.clear()
# print(cabinet)


# # 튜플 --------- 변경이 되지 않음 ( 속도가 빠름 )
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")


# 집합 (set)
# 중복 안됨 , 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# # 교집합 (java 와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 ( java도 할 수 있거나 python도 할 수 있는 개발자 )
# print(java | python)
# print(java.union(python))

# # 차집합 ( java는 할 수 있지만 python은 할 줄 모르는 개발자 )
# print(java - python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요 
# java.remove("김태호")
# print(java)



# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))



from random import * 

users = range(1,21) #1부터 20까지 숫자를 생성
users = list(users) # range 이던 users가 리스트로 형변화
shuffle(users)
winners = sample(users, 4) # 4명 중에서 1명은 치킨 3명은 커피
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")


