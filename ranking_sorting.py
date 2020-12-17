import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([500, 1000, 1500], index=['a', 'c', 'b'])
print ser1

#sorting by index
print ser1.sort_index()

#sort by values
print ser1.sort_values()

#ranking of series
print ser1.rank()

ser2 = Series(randn(10))
ser3 = ser2
print ser2

print ser2.rank()
print "sort by values and Rank"
ser2 = ser2.sort_values()
print ser2.rank()

print "sort by index and Rank "
ser3 = ser3.sort_index()
print ser3.rank()


