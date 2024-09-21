import numpy as ns
def myadd(x, y):
    return x+y

myadd = ns.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

def mysub(x, y):
    return x - y

mysub = ns.frompyfunc(mysub, 2, 1)
print(mysub([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

