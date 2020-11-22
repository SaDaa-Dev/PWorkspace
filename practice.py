
# pow 앞자리 수의 뒷자리 승 
# min , max
# round  반올림
# floor 내림
# ceil 올림
# sqrt 제곱근 명령어

# 랜덤함수
# random()   << 0.0 ~ 1.0 미만의 임의의 값 생성
# random()*10   << 0.0 ~ 10.0 미만의 임의의 값 
# random(int(random()*10)) 0 ~ 10 미만의 임의의 값 생성
# random(int(random()*10) + 1) 1 ~ 10 이하의 임의의 값 생성

# randrange(1, 46) 1 ~ 46 미만의 임의의 값 생성
# randint(1, 45) << 1 ~ 45 이하의 값을 생성

# jumin = '990120-1234567'

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])  #문자열 슬래싱


# ------------------------------------------------------------
# 문자열 관련
# ------------------------------------------------------------
# python = "Python is Amazing"
# print(python.lower()) # 모두 소문자로
# print(python.upper()) # 모두 대문자로
# print(python[0].isupper()) # 소문자인가 boolean 타입으로 반환
# print(len(python))
# print(python.replace("Python", "java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java")) #포함 되어있지 않을 경우 -1 을 반환한다.
# # print(python.index("Java")) #index 에서는 오류를 내면서 프로그램이 종료된다.

# print(python.count("n"))
# ------------------------------------------------------------

# 문자열 다루기
# #방법 1
# print("나는 %d살입니다" % 20)
# print("나는 %s를 좋아해요" % "파이썬")
# print("Apple 은 %c로 시작해요" % "A")
# # 값 2개
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# #방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법 3
# print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color= "빨간색"))
# print("나는 {age}살이며, {color}색을 좋아해요" .format(color= "빨간색", age = 20 ))

#방법 4(v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")


# 탈출문자 
# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

#저는 "나도코딩" 입니다
# print("저는 '나도코딩'입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")
# print("저는 \'나도코딩'\ 입니다")

# # \\ : 문장 내에서 \
# print("C:\\User\\Nadocoding\\Desktop\\PythonWorkspace>")

# # \r : 커서를 맨 앞으로 이동 
# print("Red Apple \rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

# 퀴즈 ------------------------------------------------------

# url = "http://naver.com"

#내방법
# index = url.find("/")+2
# print(url[index:])
# index1 = url.find(".")
# print(url[index:index1])
# three = url[index:index1-2]

# re = "%s%d%d!" %(three,len(url[index:index1]),url.count("e"))
# print(re)

# #영상방법
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5 직전까지
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다" .format(url,password))

# 퀴즈 ------------------------------------------------------








