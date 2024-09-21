
import numpy as nk
# a = nk.array([1, 2, 3, 4, 5])
# b = nk.array([1, 2, 3, 4, 5])

# # c = nk.add(a, b)
# d = nk.sum([a, b])
# print(d)

#Summation over axis
# axis = 1
e = nk.array([1, 2, 3])
f = nk.array([1, 2, 3])
g = nk.sum([e, f], axis = 1)
print(g)

#Cummulative sum
h = nk.array([1, 2, 3])
i = nk.cumsum(h)
print(i)