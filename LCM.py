import numpy as es
num1 = 23
num2 = 27

a = es.lcm(num1, num1)
print(a)

# Finding LCM in Arrays
b = es.array([3, 6, 9]) 
c = es.lcm.reduce(b)
print(c)

# Find the LCM of all values of an array where the array contains all integers from 1 to 20

d = es.arange(1, 21)
e = es.lcm.reduce(d)
print(e)