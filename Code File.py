import pandas as pd

"""This python script read ten(10)sheet from excel file named 'Input File.xlsx'
 and produce ten(10).csv file of each sheets in the excel file.
 
 XLSX_File is a variable name that store the excel file.
 
 header=None remove unnamed column, 
 Sheet1 to Sheet10 are variable names that stores each sheet in excel file.
 """

XLSX_File = pd.ExcelFile('Input File.xlsx')
Sheet1 = pd.read_excel(XLSX_File, 'Sheet1', header=None)
Sheet2 = pd.read_excel(XLSX_File, 'Sheet2', header=None)
Sheet3 = pd.read_excel(XLSX_File, 'Sheet3', header=None)
Sheet4 = pd.read_excel(XLSX_File, 'Sheet4', header=None)
Sheet5 = pd.read_excel(XLSX_File, 'Sheet5', header=None)
Sheet6 = pd.read_excel(XLSX_File, 'Sheet6', header=None)
Sheet7 = pd.read_excel(XLSX_File, 'Sheet8', header=None)
Sheet8 = pd.read_excel(XLSX_File, 'Sheet8', header=None)
Sheet9 = pd.read_excel(XLSX_File, 'Sheet10', header=None)
Sheet10 = pd.read_excel(XLSX_File, 'Sheet10', header=None)


"""Output of Sheets inside the Input File.xlsx before saving
as .csv file.
'\n' is line break in python for easy readability of output
"""
print 'Sheet1 Output'
print Sheet1, '\n'

print 'Sheet2 Output'
print Sheet2, '\n'

print 'Sheet3 Output'
print Sheet3, '\n'

print 'Sheet4 Output'
print Sheet4, '\n'

print 'Sheet5 Output'
print Sheet5, '\n'

print 'Sheet6 Output'
print Sheet6, '\n'

print 'Sheet7 Output'
print Sheet7, '\n'

print 'Sheet8 Output'
print Sheet8, '\n'

print 'Sheet9 Output'
print Sheet9, '\n'

print 'Sheet10 Output'
print Sheet10

""""Save each Sheet as .csv"""
Sheet1.to_csv('Sheet1.csv')
Sheet2.to_csv('Sheet2.csv')
Sheet3.to_csv('Sheet3.csv')
Sheet4.to_csv('Sheet4.csv')
Sheet5.to_csv('Sheet5.csv')
Sheet6.to_csv('Sheet6.csv')
Sheet7.to_csv('Sheet7.csv')
Sheet8.to_csv('Sheet8.csv')
Sheet9.to_csv('Sheet9.csv')
Sheet10.to_csv('Sheet10.csv')



"""The second faster & easiest way to achieve this with for loop iteration
NOTE: 
Comment out the above code without commenting import pandas as pd at the top
to test the following code or perhaps just run it without commenting.
"""
xlsxfile = pd.ExcelFile('Input File.xlsx')
total_sheet = len(xlsxfile.sheet_names) #get number of sheets in Input File.xlsx

for i in range(total_sheet): #loop through range of total sheet that is 10
    xlsxfile = pd.ExcelFile('Input File.xlsx')
    sheet = pd.read_excel(xlsxfile, 'Sheet' + str(i+1), header=None) #str(i+1) integer to string for reading of exact Sheet name from xlsx
    print 'Sheet' + str(i+1) + ' Output'
    print sheet, '\n'
    sheet.to_csv('Sheet' + str(i+1) + '.csv') # #str(i+1) integer to string for saving of exact Sheet name