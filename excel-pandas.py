import pandas as pd

#Handling Excel Sheets in Python
#xlrd
#openpyxl

excelfile = pd.ExcelFile('demo2.xlsx')
dframe = excelfile.parse('demo2')
print dframe
