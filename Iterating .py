#Iterating !-D Array
import numpy as ge

arr1 = ge.array([1 , 2, 3])
for a in arr1:
    print(a)

#Iterating 2-D Array
arr2 = ge.array([[1, 2, 3],[4, 5, 6]])
for b in arr2:
    print(b)

#To return the actual values, the scalars, we have to iterate the arrays in each dimension.
arr3 = ge.array([[1, 2, 3],[4, 5, 6]])
for c in arr3:
    for d in c:
        print(d)

#Iterating 2-D Array
arr4 = ge.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
for e in arr4:
  print(e)

arr5 = ge.array([[[1, 2, 3],[4 , 5, 6]],[[7, 8, 9],[10, 11, 12]]])
for i in arr5:
    for j in i:
        for k in j:
            print(k)

# Iterating Arrays Using nditer()function
arr6 = ge.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])
for a in ge.nditer(arr6):
    print(a)


# Iterating Array With Different Data Types
arr6 = ge.array([1, 2, 3])
for i in ge.nditer(arr6, flags =['buffered'], op_dtypes=['S']):
    print(i)


# Iterating With Different Step Size
arr7 = ge.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in ge.nditer(arr[:, ::2]):
  print(x)


arr8 = ge.array([1, 2, 3])
for idx, x in ge.ndenumerate(arr8):
    print(idx, x)

arr9 = ge.array([[1, 2, 3, 4],[5, 6, 7, 8]])
for idx,x in ge.ndenumerate(arr9):
    print(idx, x)


