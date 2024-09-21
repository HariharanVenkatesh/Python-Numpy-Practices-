import numpy as df
a = df.array([10, 15, 20, 25, 5])
b = df.diff([a])
print(b)

c = df.array([10, 15, 25, 5])
d = df.diff([c], n = 2)
print(d)