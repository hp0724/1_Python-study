# animal="강아지"
# name ="연탄이"
# age=4
# hobby="산책"
# is_adult=age>=3

'''
주석 처리는 #과 ' 3개 
ctrl + / 도 주석 
'''
# print("우리집 "+ animal+"의 이름은"+name+"이에요")
# print(name+"는"+str(age)+"살이며"+hobby+"을 아주 좋아해요")
# print(name +"는 어른일까요?"+str(is_adult))

# station="사당"
# print(station+"행 열차가 들어오고 있습니다.")


# ------------------------------ 연산 


# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)
# print(2**3)
# print(5%3)
# print(5//3)

# print(10>3)
# print(4>=7)
# print(10<3)
# print(5<=5)

# print(3==3)
# print(4==2)
# print(not(3!=4))

# print ((3>0) and (4>3)) 
# print ((3>0) & (4>3)) 
# print ((3>0) or (4>3)) 
# print ((3>0) | (4>3)) 

# print(abs(-5)) # 절대값 
# print(pow(4,2)) # 4^2
# print(max(5,12))
# print(min(5,12))
# print(round(3.14))

# from math import * 
# print (floor(4.99)) # 내림
# print(ceil(3.14)) # 올림 
# print(sqrt(16)) #제곱근 


# ------------------------------ 랜덤 
from random import * 
# print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성 
# print(random()*10) # 0.0 ~10.0 미만의 임의의 값 생성 
# print(int(random()*10)) # 0.0 ~10.0 미만의 임의의 값 생성 
# print(int(random()*10)+1) # 1.0 ~10.0 이하의 임의의 값 생성 
# print(int(random()*10)+1) # 1.0 ~10.0 이하의 임의의 값 생성 
# print(int(random()*10)+1) # 1.0 ~10.0 이하의 임의의 값 생성 
# print(int(random()*10)+1) # 1.0 ~10.0 이하의 임의의 값 생성 

# print(randrange(1,46)) # 1~46 미만의 임의 값 생성 
# print(randint(1,45)) # 1~46 미만의 임의 값 생성 


# ------------------------------ 문자열 
# jumin = "980724-1212414"
# print("성별 "+jumin[7])
# print("생년월일:"+jumin[:6])#처음부터 6직전까찌 
# print("뒤 7 자리 :"+ jumin[7:])
# print("뒤 7 자리 :"+ jumin[-7:])
 

python = "Python is amazing "
# print(python.lower())
# print(python.upper())
# print(python.capitalize())
# print(python[0].isupper())
# print(len(python))

# index = python.index("n")
# print(index)

# index = python.index("n",index+1)
# print(index)

# print(python.find("java"))
# print(python.index("java"))


# ------------------------------ formating 

# 방법1 
# print("나는 %d 살입니다 "%20)
# print("나는 %s을 좋아해요 "%"파이썬")
# print("apple 은 %c로 시작해요 " %"a")
# print("나는 %s색과 %s 색을 좋아해요 "%("파란","빨간"))

# 방법2 
# print("나는 {} 살입니다".format(20))
# print("나의 이름은 {} 입니다".format("수하"))
# print("나는 {0}색과 {1}색을 좋아해요 ".format("파란","빨강"))

#방법3 

# print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20,color="빨간"))

# #방법 4 
# age= 20 
# color ='빨강' 
# print(f"나는 {age}살이며, {color}색을 좋아해요 ")


# 탈출 문 
# \"   \' 문장내에서 따옴표  
print("백문이 불여일견 \n백견이 불여일타")

print("저는 \"황수하\" 입니다 ")
# 주소 칠떄는 \\ 두번 해서 출력해라 
print("\\")

# \r 커서를 맨 앞으로 이동 
print("red apple \rpine")

# \b 백스페이스 (한 글자 삭제 )
print("redd\b apple")

#\t 탭
print("red\tapple")
