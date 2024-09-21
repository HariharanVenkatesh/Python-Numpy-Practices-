import numpy as zx
a = zx.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = zx.unique(a)
print(b)


c = zx.array([1, 2, 3, 4, 5, 6, 7])   
d = zx.array([3, 4, 5, 6, 7, 8, 9])   
e = zx.union1d(c, d)                          # Finding Union
f = zx.intersect1d(c, d, assume_unique=True)  # Finding Intersection
g = zx.setdiff1d(c, d, assume_unique=True)    # Finding Difference
h = zx.setxor1d(c, d, assume_unique=True)     # Finding Symmetric Difference
# print(e)
# print(f)
print(g)