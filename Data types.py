import numpy as np
arr1 = np.array([1, 2, 3, 4])
print(arr1.dtype)

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)    #U - unicode string

arr3 = np.array([1, 2, 3, 4], dtype = 'S')  #S - string
print(arr3)
print(arr3.dtype)

#For i, u, f, S and U we can define size as well.
arr4 = np.array([1, 2, 3, 4], dtype = 'i4') #i - integer
print(arr4)
print(arr4.dtype)

arr5 = np.array([1.1, 2.1, 3.1])
newarr = arr5.astype('i')
print(newarr)
print(newarr.dtype)

arr6 = np.array([.1, 2.1, 3.1])
newarr = arr6.astype(int)
print(newarr)
print(newarr.dtype)

arr6 =np.array([1, 0, 3])
newarr = arr6.astype(bool)
print(newarr)
print(newarr.dtype)

a = np.array([1, 2])
print("Integer Datatype: ")
print(a.dtype)

b = np.array([1.0, 2.0])
print("\nFloat Datatype: ")
print(b.dtype)

c = np.array([1, 2], dtype = np.int64)
print("\nForcing Datatype: ")
print(c.dtype)

