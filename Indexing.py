#NumPy Array Indexing
# Access Array Elements
import numpy as np
arr1 = np.array([1, 2, 3, 4])
print(arr1[0])
print(arr1[1])
print(arr1[2] + arr1[3])

# Access 2-D Arrays 
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd Element on 1st row: ",arr2[0, 1])
print('3rd element on 2nd row: ', arr2[1, 4])

#Access 3-D Arrays
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3[0, 1, 2])
print(arr3[1, 1, 2])

# Negative Indexing
arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr4[1, -1])
