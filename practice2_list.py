# 리스트 []

# subway = ["유재석","조세호","박명수"]
# print(subway)
# print(subway[0])
# print(subway.index("조세호"))

# # 하하 씨 추가 
# subway.append("하하")
# print(subway)

# # 정형돈 씨를 유재석/ 조세호 사이에 태워라 
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명? 

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능 
# num_list =[5,2,3,4,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기도 가능 
# num_list.reverse()
# print(num_list)

# # 모두 지우기 
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용 
# mix_list=["조세호",20,True]
# num_list = [5,4,3,2,1]
# print(mix_list+num_list)

#------------------------------------------------------------------

# 사전 - 딕셔너리 

# 키에 대한 중복은 없다 
#cabinet = {1:"유재석",2:"박명수"}
# print(cabinet[1])
# print(cabinet.get(1))
# print(cabinet[5])
# cabinet = {"A":"유재석","B":"박명수"}
# print("A" in cabinet)  # 키 있으면 true 
# print("B" in cabinet) # 키 없으면 false 
# # 새 손님 
# print(cabinet)
# cabinet["C"]="조세호"
# print(cabinet)
# cabinet['A']="김종국"
# print(cabinet)

# # 손님 떠남 
# del cabinet["C"]
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())
# print(cabinet)

# # 목욕탕 영업 정지 
# cabinet.clear()
# print(cabinet)

#------------------------------------------------------------------

# 튜플은 변경이 불가능 하지만 리스트보다 속도가 빠르다 

# menu =("돈까스","치즈돈까스")
# print(menu[0])
# print(menu[1])
# print(menu)

# name ="황수하"
# age= 25
# hobby ="코딩"
# print(name,age,hobby)

# (name,age,hobby)=("황수하",25,"코딩")
# print(name,age,hobby)


#------------------------------------------------------------------
# 집합 (set)
# 중복 안됨 순서 없음 

# my_set={1,2,3,4,5}
# my_set2={1,1,2,3,4}
# print(my_set)
# print(my_set2)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# # 교집합 출력
# print(java & python)
# print(java.intersection( python))

# #합집합 출력 
# print(java | python )
# print(java.union(python))

# # 차집합 
# print(java - python)
# print(java.difference(python))


# # python 할 줄 아는 사람이 늘어남 
# python.add ("하하")
# print(python)

# # java를 까먹었어요 
# java.remove("김태호")
# print(java)


#------------------------------------------------------------------

# 자료 구조의 변경 

menu ={"커피","우유","주스"}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu =tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))
