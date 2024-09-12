import numpy as DS

arr = DS.array([1, 2, 3, 4, 5, 6])
# a = DS.array_split(arr, 2)
# b = DS.array_split(arr, 4)
# print(b)
# print(a)
c = DS.array_split(arr, 3)
print(c[0])
print(c[1])
print(c[2])

arr2 = DS.array([[1, 2],[3, 4],[5, 6],[7, 8],[9, 10],[11, 12]])
x = DS.array_split(arr2, 3)
print(x) 

arr3 = DS.array([[1, 2 ,3],[4, 5 ,6],[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18]])
y = DS.array_split(arr3 ,3)
print(y)

arr4 = DS.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18]])
# z = DS.array_split(arr4, 3, axis=1)
# print(z)
d = DS.hsplit(arr4, 3)
print(d)
