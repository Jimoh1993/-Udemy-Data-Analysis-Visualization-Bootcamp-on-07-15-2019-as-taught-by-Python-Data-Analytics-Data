#import numpy
#print(numpy.array([1, 2]))

import numpy as np
my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]
my_array = np.array([my_list1, my_list1])
print(my_array)
print(my_array.shape)
print(my_array.dtype)
#my_array1 = np.zeros(5)
#my_array1 = np.ones([5, 5])
#my_array1 = np.empty(5)
#my_array1 = np.eye(5)
my_array1 = np.arange(5, 51, 3)
print(my_array1)
