from numpy import random
a = random.chisquare(df = 2, size=(2, 3))
print(a)

from numpy import random
import matplotlib.pyplot as abcd
import seaborn as efg

efg.distplot(random.chisquare(df = 1, size = 1000), hist = False)
abcd.show()