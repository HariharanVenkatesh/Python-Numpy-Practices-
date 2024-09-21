import numpy as om

a = 6
b = 9

c = om.gcd(a, b)
print(c)

# Finding GCD in Arrays
d = om.array([20, 8, 32, 36, 16])
e = om.gcd.reduce(d)

print(e)