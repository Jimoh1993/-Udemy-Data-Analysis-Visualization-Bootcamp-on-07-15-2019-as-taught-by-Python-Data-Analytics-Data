## OBJECTIVE ##
#importing csv as dataframe
#using readtable of pandas
#reading partial rows of a csv file
#dumping data into a new csv file
#selecting specific columns of a csv file

import  numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.read_csv('demo.csv')
print dframe

# If the header of csv file is not present use header=None
dframe = pd.read_csv('demo.csv', header=None)
print dframe

#using readtable function
dframe2 = pd.read_table('demo.csv', sep=',', header=None)
print dframe2

#Partial rows importing / reading
print pd.read_csv('demo.csv', nrows=2, header=None)

#dumping
dframe2.to_csv('outputCSV.csv', sep=',')

#selecting specific columns of cvs file
dframe.to_csv('dataoutput.csv', columns=[0, 1])


