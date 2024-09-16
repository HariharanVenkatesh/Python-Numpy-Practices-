from numpy import random
a = random.exponential(scale = 2, size =(2, 3))
print(a)


from numpy import random
import matplotlib.pyplot as nan
import seaborn as ku

ku.distplot(random.exponential(size = 1000), hist = False)
nan.show()