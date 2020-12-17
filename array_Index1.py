import numpy as np
arr = np.arange(0, 12)
# print(arr)
# Index Slicing
# print(arr[0:6])
#Index data replace
arr[0:5] = 20
# print(arr)

#Interesting thing & important
arr2 = arr[0:6]
# print(arr2)

arr2[:] = 29 #all element are modified
# print(arr2)
print(arr)

#creating new array copy
arrcopy = arr.copy()
print(arrcopy)
