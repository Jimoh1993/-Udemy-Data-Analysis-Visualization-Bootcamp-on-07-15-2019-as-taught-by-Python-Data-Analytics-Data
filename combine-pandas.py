import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([5, np.nan, 6, np.nan], index=['A', 'B', 'C', 'D'])
print s1

s2 = Series(np.arange(4), dtype=np.float64, index=s1.index)
print s2

s3 = Series(np.where(pd.isnull(s1), s2, s1), index=s1.index)
print s3

#using combine() to achive np.where() in series
s4 = s1.combine_first(s2)
print s4

#DataFrame using combine()
df_5m = DataFrame({'col1': [5, np.nan, 15],
                   'col2': [20, 25, np.nan],
                   'col3': [np.nan, np.nan, 35]
                   })
df_10m = DataFrame({'col1': [0, 10, 20],
                    'col2': [10, 20, 30]
                    })
print df_5m

print df_10m

print df_5m.combine_first(df_10m)

# print df1
# LeftCsv = pd.read_csv('Employees-Who-Have-Left.csv', nrows=0).columns

# #Get rid of Unnamed columns in two csv files
# cols = pd.read_csv(ExCsv, nrows=1).columns
# df = pd.read_csv(ExCsv, usecols=cols[1:])
# print df


# Emplopyee Dataset cobimed together as one Dataset
# df1 = pd.DataFrame(ExCsv)
# df2 = pd.DataFrame(LeftCsv)
# frames = [df1, df2]
# Combined_EmployeesDataset = pd.concat(frames, ignore_index=False)
# Combined_EmployeesDataset.to_csv('Combined-Employees-Dataset.csv', encoding='utf-8')
#
# ExCsv = pd.read_csv('Existing-Employees.csv', nrows=1).columns #Get rid of Unnamed Columns in csv files
# ExCsv = pd.read_csv('Existing-Employees.csv', usecols=ExCsv[1:])

