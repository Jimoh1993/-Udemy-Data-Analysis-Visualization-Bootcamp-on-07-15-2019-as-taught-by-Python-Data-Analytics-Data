import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.random.randn(1000, 5))
print df

#basic observation by filtering
print df.head()
print df.tail()

print df.describe()

column = df[0] #
print column
# print column.head()
# print column[np.abs(column) > 3]

