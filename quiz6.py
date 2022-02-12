'''
남자 = 키(m)*키(m) *22
여자 = 키(m)*키(m) *21
조건 1 함수내에서 계산
조건 2 표준 체중은 소수점 둘째자리까지 표시 
'''

 

def std_weight(height,gender):
    if gender=="남자":
        return float(height*height*22)
    elif gender =="여자":
        return float(height*height*21)


gender = input("성별을 입력하세요 ")
height = float(input("키를 입력하세요 (m)"))
weight=std_weight(height,gender)
print(f"키 {height*100}cm {gender} 표준 체중은 {weight:.2f}kg입니다.")


