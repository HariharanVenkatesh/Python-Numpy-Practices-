import numpy as cv

arr = cv.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)

filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr2 = cv.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr2:
    if element % 2 ==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr2[filter_arr]
print(filter_arr)
print(newarr) 

arr3 = cv.array([23, 24, 25, 26])
filter_a = arr3 > 24
newarr = arr3[filter_a]
print(filter_a)
print(newarr)

arr4 = cv.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
filter_b = arr4 % 2 == 0
c = arr4[filter_b]
print(filter_b)
print(c)
