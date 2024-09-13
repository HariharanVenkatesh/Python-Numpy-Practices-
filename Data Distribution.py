from numpy import random
a = random.choice([23, 5, 73, 10], p = [0.0, 0.1, 0.3, 0.6], size = (100))
print(a)

b = random.choice([11, 23, 18, 17], p = [0.6, 0.1, 0.0, 0.3], size = (3, 6))
print(b)

c = random.choice([100, 500, 1000, 2000], p = [0.0, 0.3, 0.1, 0.6], size = (5, 5))
print(c)