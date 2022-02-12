# 함수 

# def open_account():
#     print("새로운 계좌가 생성")

# def deposit(balance,money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance+money))
#     return balance+money

# def withdraw(balance,money): # 출금 
#     if balance>=money : #잔액이 출금보다 많으면 
#         print("출금이 완료 되었습니다 잔액은 {0}".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다 잔액은 {0}".format(balance))
#         return balance

# balance = deposit(5000,500)
# balance = withdraw(balance,6000)


# 함수 기본값 

# def profile(name,age,main_lang):
#     print("이름 :{0} \t 나이:{1} \t 사용언어:{2}"\
#         .format(name,age,main_lang))


# profile("suha",24,"python")

# 같은 학교 같은 반 같은 수업 

# def profile(name,age=17,main_lang="파이썬"):
#     print("이름 :{0} \t 나이:{1} \t 사용언어:{2}"\
#         .format(name,age,main_lang))

# profile("유재석",16)
# profile("김태호")

# 키워드 값 


# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(age=15,name="suha",main_lang="python")

#---------------------------------------------------------------------------
# 가변 인자 
# def profile(name,age,*lang):
#     print(name,age)
#     for l in lang:
#         print(l,end=" ")
#     print()
# profile("황수하",24,"java","c#","c++")

# 지역변수 전역변수 
#전역 변수 
# gun = 10 
# def checkpoint(soldiers): #경계근무 
#     # 지역변수 
#     #gun=0

#     #전역변수 
#     global gun 
#     gun= gun-soldiers
#     print("[함수 내] 남은 총 :{0}".format(gun))


# def checkpoint_re(gun,soldiers):
#     gun= gun-soldiers 
#     print("[함수 내] 남은 총 :{0}".format(gun))
#     return gun

# print("전체총: {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 
# print("전체총: {0}".format(gun))
# gun=checkpoint_re(gun,2)
# print("남은총: {0}".format(gun))


# 표준 입출력 

# print("python","java",sep=",",end="\t")
# print("무엇이 더 재밌을까요?")

# import sys 
# print("python","java",file=sys.stdout)
# print("python","java",file=sys.stderr)

# scores = {"수학":0, "영어":50,"코딩":100}
# # items 는 key value 로 나누어진다 .

# for subject,score in scores.items():
#     #print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":")


# 은행 대기 순번표 

# 001 ,002 ,003 ..... 
# for num in range(1,21):
#     print("대기번호:"+str(num).zfill(3))

# 사용자 입력 값은 항상 문자열로 인식이 된다 
# answer = input("아무 값이나 입력하세요:")
# print(type(answer))
# print("입력하신 값은 "+answer+"입니다 ")


# ---------------------------------------------------------
# 다양한 format 형식 
print("{0:a>10}".format(500))
# 양수 일떄 +로 표시 음수 일떄 - 로 표시 
print("{0: >+10}".format(500))
print("{0: >-10}".format(-500))
# 왼쪽 정렬하고 ,빈칸으로 _ 로채움 
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000000000000))

# 3자리 마다 콤마를 찍어주기 부호도 붙여주기
print("{0:+,}".format(10000000000000000000))
print("{0:+,}".format(-10000000000000000000))

print("{0:^<+30,}".format(1000000000000000))

# 소수점 출력 
print("{0:f}".format(5/3))
# 특정소수점 까지만 출력 
print("{0:.2f}".format(5/3))
