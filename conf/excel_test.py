# import pandas as pd
#
# excel_file = 'excel_test.xlsx'
#
# df = pd.DataFrame(pd.read_excel(excel_file))
# print(df)
#
# print(type(df))

import xlrd
data = xlrd.open_workbook('excel_test.xlsx')
tables = data.sheets()[0]
print(tables.nrows)


print(tables.row_values(2))
x = tables.row_values(2)
print(type(x))

print(x[0])