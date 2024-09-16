from numpy import random
a = random.uniform(size = (2, 3))
print(a)

# Visualization of Uniform Distribution
from numpy import random
import matplotlib.pyplot as asd
import seaborn as mp

mp.distplot(random.uniform(size = 1000), hist = False)
mp.distplot(random.uniform(size = 500), hist = False)
asd.show()