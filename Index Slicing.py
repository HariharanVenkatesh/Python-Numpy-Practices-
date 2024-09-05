#NumPy Array Slicing
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, 6, 7]) 
print(arr1[1:5])
print(arr1[4:])
print(arr1[:4])
print(arr1[-3:-1])
print(arr1[1:5:2])
print(arr1[::2])

# Slicing 2-D Arrays

arr2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(arr2[1, 1:4])
print(arr2[0:2, 2])
print(arr2[0:2, 1:4])

arr3= np.array([[-1, 2, 0, 4],[4, -0.5, 6, 0],[2.6, 0, 7, 8],[3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr3)

slicing_arr = arr3[:2, ::2]
print("Array with first two rows and"
      " alternate colums(0 and 2):\n",slicing_arr)