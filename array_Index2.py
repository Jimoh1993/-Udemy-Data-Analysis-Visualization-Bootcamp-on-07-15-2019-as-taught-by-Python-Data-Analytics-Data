import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

# slices of 2d array
slice1 = arr2d[0:2, 0:2]
# print(slice1)

arr2d[:2, 1:] = 15
# print(arr2d)

# using loop to index
arr_len = arr2d.shape[0]
for i in range(arr_len):
    arr2d[i] = i
print(arr2d)

# one way to accessing row
print(arr2d[[0, 1]])
print(arr2d[[2, 0]])
