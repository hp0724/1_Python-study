'''
50명의 승객과 매칭 기회가 있을떄 

조건1 승객별 운행 시간 5분~50분 
조건2 소요시간 5분 ~15분 사이의 승객만 매칭 




'''
# 내가 푼 문제 

# from random import*
# customer=[0]*51
# cnt=0 #총 탑승 승객수 
# for i in range(1,51): # 1~50 이라는 수 
#     customer[i]=int(50*random())
#     if(customer[i]>=5 and customer[i]<=15):
#         print("[0] {0}번쨰 손님 (소요시간: {1}분)".format(i,customer[i]))
#         cnt+=1
#     else:
#         print("[ ] {0}번쨰 손님 (소요시간: {1}분)".format(i,customer[i]))
# print("총 탑승 승객:{0} 분".format(cnt))


# 답안 
from random import*
cnt =0 
for i in range(1,51):
    time = randrange(5,51)
    if 5<=time <=15: #5분 ~15분이내의 손님 ,탑승 수 증가 처리 
        print("[0] {0}번쨰 손님 (소요시간 : {1}분".format(i,time))
        cnt +=1 
    else :  #매칭 실패한경우 
        print("[ ] {0}번쨰 손님 (소요시간 : {1}분".format(i,time))

print("총 탑승 승객 :{0} 분".format(cnt))