"""
import numpy as mo
# a = mo.arange(1, 10)
# b = mo.arange(1,10)
# print(mo.log2(a))          #Log at Base 2
# print(mo.log10(b))         #Log at Base 10

#Natural Log or Log at base e
c = mo.arange(1, 10)
print(mo.log(c))
"""
#Log at any Base
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))