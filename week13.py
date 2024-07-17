# 변수도 가져쓸 수 있는지 질문 8줄

import math
import random
import numpy as np

import def_star as ds # 내가 만든 .py 파일도 가져다 사용할 수 있다
# 파이썬 파일 이름이 숫자로 시작하면 import 불가

from def_star import amount, make_star, aa # 가져다 쓰고 싶으면 이렇게도 사용 ㄱㄴ

a = math.cos(math.pi)
print(a)

b = random.randint(1, 10) # 1 ~ 10 사이에서 랜덤하게 뽑음
print(b)

c = np.array([1,2,3])
print(c)

ds.make_star(5)

print(ds.aa)
print(aa)

hap = amount(3,5)
print(hap)