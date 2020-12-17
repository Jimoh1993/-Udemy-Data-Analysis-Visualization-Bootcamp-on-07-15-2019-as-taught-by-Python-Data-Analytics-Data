#Merging Dataset on columns
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df_1 = DataFrame({'reference': ['O', 'U', 'L', 'O', 'U'],
                  'data': range(5)})
print df_1

df_2 = DataFrame({'profit': [10, 20]},
                 index=['O', 'U'])
print df_2

print pd.merge(df_1, df_2, left_on='reference', right_index=True)

df_3 = DataFrame({'ref1': ['A', 'A', 'O', 'O', 'A'],
                  'ref2': [5, 10, 15, 20, 25],
                  'ref3': [0, 1, 2, 3, 4]})

df_4 = DataFrame(np.arange(10).reshape(5, 2), index=[['A', 'A', 'O', 'O', 'O'], [20, 10, 10, 10, 20]], columns=['col1', 'col2'])

print pd.merge(df_3, df_4, left_on=['ref1', 'ref2'], right_index=True)

#join function: to use join function dataframes must
# be in thesame size or dimension
#with join it reduce args compare to merge
df_5 = DataFrame({'ref1': ['A', 'A', 'A', 'O', 'O'],
                  'ref2': [5, 10, 15, 20, 25],
                 'ref3': np.arange(5)})

df_6 = DataFrame({'ref1': ['A', 'A', 'O', 'O', 'O'],
                  'ref2': [15, 20, 25, 30, 55],
                  'ref3': [2, 3, 4, 5, 6]})
print df_5.join(df_6, lsuffix='x', rsuffix='y')
