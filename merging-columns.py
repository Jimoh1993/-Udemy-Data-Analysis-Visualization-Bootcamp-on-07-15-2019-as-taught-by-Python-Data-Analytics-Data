#Merging Dataset on columns
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#many to one merging
dframe1 = DataFrame({'reference': ['ola', 'uber', 'lyft', 'gojek', 'grab'], 'revenue': [1, 2, 3, 4, 5]})
dframe2 = DataFrame({'reference': ['ola', 'uber', 'uber', 'ola'], 'revenue': [1, 2, 3, 4]})

# print dframe1
# print dframe2

df3 = pd.merge(dframe1, dframe2, on='reference')
# print df3

df4 = pd.merge(dframe1, dframe2, on="reference", how="left")
# print df4

df5 = pd.merge(dframe1, dframe2, on="reference", how="right")
# print df5

df6 = pd.merge(dframe1, dframe2, on="reference", how="outer")
# print df6

#Many to Many Merging
df7 = DataFrame({'reference': ['ola', 'ola', 'lyft', 'lyft', 'uber', 'uber', 'ola'],
                 'revenue': [1, 2, 3, 4, 5, 6, 7]})
df8 = DataFrame({'reference': ['uber', 'uber', 'lyft', 'ola', 'ola'],
                 'revenue': [1, 2, 3, 4, 5]})
# print df7
# print df8
# print pd.merge(df7, df8) #this merge follow index df7 value that matches df8 value

#multiple references
df9 = DataFrame({'reference': ['ola', 'ola', 'lyft'],
                 'revenue': ['one', 'two', 'three'],
                'profit': [1, 2, 3]})

df10 = DataFrame({'reference': ['ola', 'ola', 'lyft', 'lyft'],
                 'revenue': ['one', 'one', 'one', 'three'],
                  'profit': [4, 5, 6, 7]})
print df9
print df10
print pd.merge(df9, df10, on=['reference', 'revenue'], how="outer")

print pd.merge(df9, df10, on=['reference', 'revenue'], how="outer", suffixes=('_first', '_second'))

