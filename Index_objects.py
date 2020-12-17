import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#Learning how to index in Pandas

series1 = Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print series1

index1 = series1.index
print index1

print index1[2:]
#
# #Negative Index
print index1[-2:]
print index1[:2]

print index1[2:4]

#Interesting  but index in dataframe cant be change
index1[0] = '0'
print index1