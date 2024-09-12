import numpy as nd

arr1 = nd.array([1, 2, 3])
arr2 = nd.array([4, 5, 6])
arr = nd.concatenate((arr1, arr2))
print(arr)

arr1 = nd.array([[1, 2],[3, 4]])
arr2 = nd.array([5, 6],[7, 8])
arr = nd.concatenate((arr1, arr2), axis=1)
print(arr)

#Joining Arrays Using Stack Functions
arr1 = nd.array([1, 2, 3])
arr2= nd.array([4, 5, 6])
arr = nd.stack((arr1, arr2), axis=1)
print(arr)

# stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
arr1 = nd.array([1, 2, 3])
arr2 = nd.array([4, 5, 6])
arr = nd.hstack((arr1, arr2))
print(arr)

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
arr1 = nd.array([1, 2, 3])
arr2 = nd.array([4, 5, 6])
arr = nd.vstack((arr1, arr2))
print(arr)

#Stacking Along Height(Depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr1 = nd.array([1, 2, 3])
arr2 =nd.array([4, 5, 6])
arr = nd.dstack((arr1, arr2))
print(arr)
