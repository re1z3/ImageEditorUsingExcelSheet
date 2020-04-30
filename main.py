from PIL import Image,ImageFont,ImageDraw
import xlrd

path = "emails.xlsx"

inputWorkBook= xlrd.open_workbook(path)
inputWorkSheet= inputWorkBook.sheet_by_index(0)

rows=inputWorkSheet.nrows
    #cols=inputWorkSheet.ncols
names=[]
for i in range(0,rows):
    names.append(inputWorkSheet.cell_value(i,0))

for j in names:
    str1=j
    img= Image.open('P.png')
    font= ImageFont.truetype("arial.ttf",25)
    width,height=font.getsize(str1)
    w=500/2
    h=480/2
    draw=ImageDraw.Draw(img)
    draw.text((w,h),str1,font=font,fill='#D4AF37')

    img.show()
    #img.save('{}.png'.format(j))




