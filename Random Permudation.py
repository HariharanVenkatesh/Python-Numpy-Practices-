from numpy import random
import numpy as gh
a = gh.array([21, 22, 23, 24, 25])
random.shuffle(a)
print(a)

b = gh.array([10, 20, 30, 40, 50, 60, 70])
print(random.permutation(b))