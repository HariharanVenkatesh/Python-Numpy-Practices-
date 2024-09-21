import numpy as pv
a = pv.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
b = pv.array([21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

c = pv.add(a, b)         # For addition
d = pv.subtract(a, b)    # For subraction
e = pv.multiply(a, b)    # For Multiplication
f = pv.divide(a, b)      # For Devition
g = pv.power(a, b)       # For Power
h = pv.mod(a, b)         # For remainder
i = pv.remainder(a, b)   # For remainder
j = pv.divmod(a, b)      # For Quotiant&Reminder
k = pv.absolute(a, b)    # For Absolute Value

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)