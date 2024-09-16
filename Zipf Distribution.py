from numpy import random
x = random.zipf(a = 2, size = (2, 3))
print(x)

from numpy import random 
import matplotlib.pyplot as kgf
import seaborn as db

x = random.zipf(a = 2, size = 1000)
db.distplot(x[x<20], kde = False)
kgf.show()