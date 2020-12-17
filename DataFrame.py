import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#Example revenue of companies
revenue_df = pd.read_clipboard()
print revenue_df

#index and columnns
print revenue_df.columns
print revenue_df['Rank']

#multiple columns
print DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry'])

#nan Values
revenue_df2 = DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry', 'Profit'])
print revenue_df2

#head and tail
print revenue_df.head(2)
print revenue_df.tail(2)

#access rows in df
print revenue_df.ix[0] #row 1
print revenue_df.ix[5] #row 6

#assign values to df
#numpy
array1 = np.array([1, 2, 3, 4, 5, 6])
revenue_df2['Profit'] = array1
print revenue_df2

#series
profits = Series([900, 1000], index=[3, 5])
revenue_df2['Profit'] = profits

print revenue_df2

#deletion from DataFrame
del revenue_df2['Profit']
print revenue_df2

#dictionary function to dataframe
sample = {
    'company': ['A', 'B'],
    'Profit': [1000, 5000]
}

print sample

sample_df = DataFrame(sample)
print sample_df
