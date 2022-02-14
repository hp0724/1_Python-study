'''
치킨 자동 주문 시스템 

조건1 : 1보다 작거나 숫자가 아닌 입력값은 ValueError

조건2 총 치킨량 10 치킨 소진시 soldError 

'''
class SoldOutError(Exception):
    pass


chicken =10 
waiting = 1 # 홀 만석 대기번호 1
while(True):
    try:
        print("남은 치킨 {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량 많음
            print("재료 부족 ")

        elif order <= 0 :
            raise ValueError
            
        else :
            print("[대기번호 {0}] {1} 마리 주문이 완료"\
                .format(waiting,order))
            
            waiting +=1
            chicken -=order


        if chicken == 0:
            raise SoldOutError
            
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다")
        break
