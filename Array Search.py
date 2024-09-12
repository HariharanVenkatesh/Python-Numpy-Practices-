import numpy as gh

arr = gh.array([1, 2, 3, 4, 5, 6, 7, 6, 8, 9, 6])
# x = gh.where(arr == 6)
# x = gh.where(arr%2 == 0)
x = gh.where(arr%2 == 1)
print(x)

# arr2 = gh.array([6, 7, 8, 9])
# x = gh.searchsorted(arr2, 7)
# x = gh.searchsorted(arr2, 7, side='right' )
arr3 = gh.array([1, 3, 5, 7])
x = gh.searchsorted(arr3, [2, 4, 6])
print(x)