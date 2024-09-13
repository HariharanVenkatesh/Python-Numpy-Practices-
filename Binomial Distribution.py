from numpy import random
x = random.binomial(n = 20, p=0.9, size = 10)
print(x)

from numpy import random
import matplotlib.pyplot as aws
import seaborn as gh
gh.distplot(random.binomial(n = 10, p = 0.2, size = 1000), hist = True, kde=False)
aws.show()
gh.distplot(random.normal(loc = 50, scale = 5, size = 1000), hist = False, label='normal')
gh.distplot(random.binomial(n = 100, p = 0.5, size = 1000), hist =False, label='binomial')
aws.show()
