import numpy as nw

arr1 = nw.array([1, 2, 3, 4, 5])
a = arr1.copy()
arr1[0] = 42
print(arr1)
print(a)

arr2 = nw.array([1, 2, 3, 4, 5])
b = arr2.view()
arr2[0] = 42
print(arr2)
print(b)

#Make Changes in the VIEW
arr3 = nw.array([1, 2, 3, 4, 5])
c = arr3.view()
c[0] = 31
print(arr3)
print(c)

#To Check if Array Owns its Data
arr4 =nw.array([1, 2, 3, 4, 5])
a = arr4.copy()
b = arr4.view()
print(a.base)
print(b.base)

