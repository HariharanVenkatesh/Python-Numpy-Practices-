from numpy import random
a = random.normal(size = (2, 3))
print(a)

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
b = random.normal(loc=1, scale=2, size=(2, 3))
print(b)

# Visualization of Normal Distribution
from numpy import random
import matplotlib.pyplot as ags
import seaborn as vjs

vjs.distplot(random.normal(size=500), hist=False)
ags.show()