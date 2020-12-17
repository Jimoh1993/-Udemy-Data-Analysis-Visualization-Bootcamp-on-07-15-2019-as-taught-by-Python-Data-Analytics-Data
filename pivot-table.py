import numpy as np
import pandas as pd
from pandas import Series, DataFrame

url = "https://en.wikipedia.org/wiki/Pivot_table"
df_list = pd.io.html.read_html(url)
df = df_list[0]

print df
#-----Below code is use to remove numerical value across column of df
#-----With lxml packages install will solve this problem without the following#-----code
# new_header = df.iloc[0] #grab the first row for the header
# df = df[1:] #take the data less the header row
# df.columns = new_header #set the header row as the df header
# print df

pt = df.pivot('Date of sale', 'Sales person', 'Total price')
print pt
