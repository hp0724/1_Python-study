# import 는 모듈이랑 패키지만 가능 
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage 
# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to= vietnam.vietnamPackage()
# trip_to.detail()


# from random import * 
# 공개 범위를 설정해야함 
from travel import *
# #trip_to= vietnam.vietnamPackage()
# trip_to= thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getabsfile(thailand))