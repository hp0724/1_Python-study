# 파일 입출력 

# utf8 한글 
# w는 덮어쓰기 
# score_file =open("score.txt","w",encoding="utf8")
# print("수학 :0",file =score_file)
# print("영어 :50",file =score_file)
# score_file.close()

# a는 이어쓰기 
# score_file =open("score.txt","a",encoding="utf8")
# # write는 줄바꿈 없음 
# score_file.write("과학 : 80 ")
# score_file.write("\n코딩 : 100 ")
# score_file.close()

# score_file =open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file =open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# score_file.close()


# while 이용해서 파일 읽기 

# score_file =open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     # 읽어오는 문장이 없으면 
#     if not line:
#         break
#     print(line,end="")
# score_file.close()


# score_file =open("score.txt","r",encoding="utf8")
# lines =score_file.readlines() # list 형태로 저장 
# for line in lines:
#     print(line,end="")

# score_file.close()



# pickle 

# import pickle
# # pickle 쓸려면 binary 로 작성  encoding은 노필요 
# profile_file =open("profile.pickle","wb")
# profile ={"이름":"박명수","나이":30,"취미":["축구","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) #profile에 있는 정보르 file에 저장 
# profile_file.close()


# profile_file =open("profile.pickle","rb")
# profile =pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기 
# print(profile)
# profile_file.close()



# with 

import pickle
# 열었던 파일에 대한 close 가 필요 없음 
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요 ")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
