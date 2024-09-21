import numpy as pd
a = pd.array([1, 2, 3, 4])
b = pd.prod(a)
print(b)

c = pd.array([1, 2, 3, 4])
d = pd.array([5, 6, 7, 8])
e = pd.prod([c, d])
print(e)

# Product Over an Axis
f = pd.array([1, 2, 3, 4])
g = pd.array([5, 6, 7, 8])
h = pd.prod([f, g], axis = 1)
print(h)

#Cummulative Product
i = pd.array([5, 6, 7, 8, 9, 10])
j = pd.cumprod([i])
print(j)
