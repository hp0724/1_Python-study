# url= "http://naver.com"
# url_1=url[7:]
# print(url_1)
# point= url_1.find(".")
# print(point)
# url_2=url_1[0:point]
# print(url_2)
# url_3 = url_2[:3]
# count_str=len(url_2)
# count_e=url_2.count("e")
# print(count_e)

# print(url_3+str(count_str)+str(count_e)+"!")


# 답안지 
url= "http://naver.com"
my_str=url.replace("http://","") # 규칙 1 
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] +str(len(my_str)) +str(my_str.count("e")) +"i"
print(password)
