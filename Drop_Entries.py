import numpy as np
import pandas as pd
from pandas import Series, DataFrame

cars = Series(['BMW', 'Audi', 'Merc'], ['a', 'b', 'c'])

print cars

cars = cars.drop('a')
print cars

#Datataframe
cars_df = DataFrame(np.arange(9).reshape(3, 3), index=['BMW', 'Audi', 'Merc'], columns=['rev', 'pro', 'exp'])
print cars_df

cars_df = cars_df.drop('BMW', axis=0)
print cars_df

cars_df = cars_df.drop('pro', axis=1)
print cars_df
