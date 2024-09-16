from numpy import random
a = random.pareto(a = 2, size = (2, 3))
print(a)

from numpy import random
import matplotlib.pyplot as bnm
import seaborn as lib

lib.distplot(random.pareto(a = 2, size = 1000), kde = False)
bnm.show()