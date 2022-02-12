class Unit:
    def __init__(self):
        print("unit 생성자")

class Flyable:
    def __init__(self):
        print("flyable 생성자")
# 두개이상의 부모클래스 를 상속받을떄는 super가 1개만됨 
class FlyableUnit(Unit,Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 
dropship = FlyableUnit()