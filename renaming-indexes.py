import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.arange(25).reshape(5, 5), index=['UBER', 'OLA', 'GRAB', 'GOJEk', 'LYFT'], columns=['RE', 'LO', 'QU', 'GR', 'AG'])
print df

#Way1 use mapping
df.index = df.index.map(str.lower)
print df

#Way2 rename method
print df.rename(index=str.title, columns=str.lower)

#Way3 using dictionary
print df.rename(index={'uber': 'The Best Taxi'}, columns={'RE': 'Revenue'})

#How to save changes
df.rename(index={'uber': 'The Best Taxi'}, columns={'RE': 'Revenue'}, inplace=True)
print df
