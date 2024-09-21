a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = []
for i, j in zip(a, b):
    c.append(i * j)
    print(i * j)
else:
    print(c)

import numpy as nk

a = [1, 2, 3, 4, 5, 6, 7]
b = [9, 8, 7, 6, 5, 4, 3]
c = nk.add(a, b)

print(c)