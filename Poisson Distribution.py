from numpy import random
a = random.poisson(lam=2, size=10)
print(a)

# Visualization of Poisson Distribution
from numpy import random
import matplotlib.pylab as ash
import seaborn as har

har.distplot(random.poisson(lam = 2, size=1000), kde=False)
ash.show()
har.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
har.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

ash.show()