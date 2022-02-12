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


def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(age=15,name="suha",main_lang="python")
