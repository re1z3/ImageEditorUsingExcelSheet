import xlrd


path = "emails.xlsx"

inputWorkBook= xlrd.open_workbook(path)
inputWorkSheet= inputWorkBook.sheet_by_index(0)

rows=inputWorkSheet.nrows
cols=inputWorkSheet.ncols
names=[]

for i in range(0,rows):
    names.append(inputWorkSheet.cell_value(i,0))

print(len(names))