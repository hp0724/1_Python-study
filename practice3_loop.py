# #분기문 

# weather = input("오늘 날씨는 어떄요?")

# '''
# if 조건: 
#     실행 
# elif 조건:
#     실행 
# else 조건:
#     실행 
# '''

# if weather=="비":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else: 
#     print("준비물 필요없어요 ")

#--------------------------------------------------------------------


# #  for 반복문 

# for waiting_no in [0,1,2,3,4,5]:
#     print("대기번호:{0}".format(waiting_no))


# # 순차적으로 커질때에는 
# # range에 시작은 0 임 
# for waiting_no in range(1,5):
#     print("대기번호 : {0}".format(waiting_no))



# starbucks = ["아이어맨","토르","아이엠 그루트","스파이더맨"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

#--------------------------------------------------------------------


# while 조건문 

# customer = "토르"
# index =5 
# # while 은 참인 경우에만 실행 
# while index >=1:
#     print("{0},커피가 준비 되었습니다 {1}번 남았어요".format(customer,index))
#     index -=1
#     if index==0:
#         print("커피는 폐기처분 ")

#--------------------------------------------------------------------

# #무한 루프 
# customer = "아이언맨"
# index = 1
# while True:
#         print("{0},커피가 준비 되었습니다 {1}번 남았어요".format(customer,index))
#         index+=1

#--------------------------------------------------------------------

# customer = "아이언맨"
# person="unknown"

# while person!=customer:
#     print("{0} 커피가 준비 되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요?")
#     if person==customer:
#         print("커피 받아가세요")
#         print()
#     else:
#         print("잠시만 기달려주세요")
#         print()

#--------------------------------------------------------------------

#continue , break 

 

# absent = [2,5] # 결석 
# no_book = [7]
# for student in range (1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지 {0}는 교무실로 따라와".format(student))
#         break
    
#     print("{0},책을 읽어봐".format(student))



#--------------------------------------------------------------------

# 한줄 for 문 
# 출석번호가 1,2,3,4 앞에 101 102 103 104 붙이기 
# student =[1,2,3,4,5]
# print(student)

# student=[i+100 for i in student]
# print(student)

# #학생 이름을 길이로 변환 
# students = ["iron man","thor","i am groot"]
# print(students)

# # 뒤에서부터 연산 생각 
# student=[len(i) for i in students]
# print(student)


students = ["iron man","thor","i am groot"]
students =[i.upper() for i in students]
print(students)


