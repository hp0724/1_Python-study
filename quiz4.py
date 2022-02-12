''' 참석률 높이기 위해 댓글 이벤트 
    댓글 작성자 1명은 치킨 3명은 커피쿠폰 
    
    조건 1 댓글 20명 작성 1~20 
    조건 2 무작위 추첨 중복 불가 
    조건 3 random모듈과 shuffle 과 sample 활용 

    예제 
    당첨자 발표 
    치킨 :1
    커피 : 2,3,4
    
    
    '''

from random import*
lst = range(1,21) # 1부터 20 까지 숫자를생성 
lst=list(lst)
print(lst)
shuffle(lst)
print(lst)
# 뽑아버리기 
winners =sample(lst,4) # 4명중에서 1명은 치킨 ,3명은 커피 

print("--- 당첨자 발표 ---")
print("치킨 당첨자 {0}".format(winners[0]))
print("커피 당첨자 {0}".format(winners[1:]))
print("--- 축하합니다 ---")
