# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
#     return balance + money

# def withdraw(balance, money) :
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_nigth(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0 #잔액
# balance = deposit(balance , 1000)
# print(balance)

# commission, balance = withdraw_nigth(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# # 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}"\
#     .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# # 키워드값을 이용한 함수 호출
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25 ,name="김태호")


# # 가변인자 ------------------------------------
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석",20,"Python","JAVA","C++","C","C#")
# profile("유재석",20,"Kotlin","JAVA")

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


#퀴즈

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    if gender == "여자":
        return height * height * 21

avgW = round(std_weight(174 / 100, "남자"), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(175,"남자",avgW))
