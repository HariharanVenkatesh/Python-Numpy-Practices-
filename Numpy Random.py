from numpy import random
a = random.randint(100)
print(a)

#Generate a random float from 0 to 1
b = random.rand()
print(b)

#Generate Random Array
#Generate a 1-D array containing 5 random Integers from 0 to 100:
from numpy import random
x = random.randint(100, size =(5))
print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
d = random.randint(100, size = (3, 5))
print(d)

#The rand() method also allows you to specify the shape of the array.
e = random.rand(5)
f = random.rand(3, 5)
print(e)
print(f)

g = random.choice([3, 5, 7, 9])
print(g)

h = random.choice([3, 5, 7, 9], size = (3, 5))
print(h)