# import pandas as pd
#
# """""If you want to read data from all sheets in an Excel file,
# you will first have to find the names of the sheets in the file.
# Then read data from each and append them all into a single DataFrame.
# After all sheets have been read, the DataFrame can be written to a CSV file.
# Following code assumes that the first line of the Excel file is the header."""
#
# df = pd.DataFrame()
# xlfname = 'sample.xlsx'
# xl = pd.ExcelFile(xlfname)
#
# for sheet in xl.sheet_names:
#     df_tmp = xl.parse(sheet)
#     df = df.append(df_tmp, ignore_index=True)
#
# print(len(df))
#
# csvfile = 'sample.csv'
# df.to_csv(csvfile, index=False)
#
#
# "Program 2"
#
# excel_files = [
#     'file1.xlsx',
#     'file2.xlsx',
#     'file3.xlsx'
# ]
#
# df = pd.concat([pd.read_excel(f) for f in excel_files])
# df.to_csv('files.csv', index=False)

#count the total number of sheets in an Excel file using Python
import pandas as pd
xlsxfile = pd.ExcelFile('Input File.xlsx')
total_sheet = len(xlsxfile.sheet_names)
print total_sheet


for i in range(total_sheet):
    xlsxfile = pd.ExcelFile('Input File.xlsx')
    sheet = pd.read_excel(xlsxfile, 'Sheet' + str(i+1), header=None)
    sheet.to_csv('Sheet' + str(i+1))
