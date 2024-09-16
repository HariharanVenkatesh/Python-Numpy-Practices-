from numpy import random
a = random.logistic(loc = 1, scale = 2, size = (2, 3))
print(a)

# # Visualization of Logistic Distribution
from numpy import random
import matplotlib.pyplot as bfg
import seaborn as nk

nk.distplot(random.logistic(size = 1000), hist = False)
bfg.show()

# Difference Between Logistic and Normal Distribution

nk.distplot(random.normal(scale = 2, size = 1000), hist = False, label = 'Normal')
nk.distplot(random.logistic(size = 1000), hist = False, label= 'logistic')
bfg.show()