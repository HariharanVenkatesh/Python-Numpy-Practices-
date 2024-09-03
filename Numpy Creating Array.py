import numpy as np

# Create a simple array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Perform an operation
squared_arr = arr ** 2
print("Squared Array:", squared_arr)

import numpy as np

print(np.__version__)

#NumPy Creating Arrays

import numpy as np
arr = np.array([6,7,8,9,10])
print(arr)
print(type(arr))



import numpy as np

# Creating a rank 1 array
arr1 = np.array([1, 2, 3])
print("Array With Rank 1: \n",arr1)

# Creating a rank 2 array
arr2 = np.array([[1, 2, 3],
             [4, 5, 6]])
print("Array With Rank 1: \n",arr2)

# Creating an array from tuple
arr3 = np.array((1, 2, 3, 4, 5))
print("Using a tuple to create a NumPy array:\n",arr3)

arr4 = np.array((1, 2, 3))
print("Array Created using "
      "Passed Tuple:\n", arr4)



# Dimensions in Arrays
# 0-D Arrays
# Creating a 0-D array
import numpy as np
arr = np.array(42)
print(arr)

# 1-D Array
# Creating a 1-D array
arr1= np.array([1, 2, 3, 4, 5])
print(arr1)

# 2-D Array
# Creating a 2-D array
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
print(arr2)

# 3-D Array
# Creating a 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)

#Higher Dimensional Arrays
arr4 = np.array([1, 2, 3, 4], ndmin=5)

print(arr4)
print('number of dimensions :', arr4.ndim)

#To Check Number of Dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

