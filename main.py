# Python script for image editor (only for single excel sheet)
# Follow the comments in the given code below to the run the image editor as per preference


from PIL import Image,ImageFont,ImageDraw
import xlrd

path = ""  # add path of the excel sheet file

inputWorkBook= xlrd.open_workbook(path)
inputWorkSheet= inputWorkBook.sheet_by_index(0) # only for a single excel sheet 

rows=inputWorkSheet.nrows  # only for rows uncomment the line just below if you want columns 
#cols=inputWorkSheet.ncols
names=[]
for i in range(0,rows):  # only for rows, add columns if required, add iterating variable if required
    names.append(inputWorkSheet.cell_value(i,0))

for j in names:
    str1=j
    img= Image.open("") # add image file and open it as per preference
    font= ImageFont.truetype("arial.ttf",25)
    width,height=font.getsize(str1)
    w=500/2
    h=480/2
    draw=ImageDraw.Draw(img)
    draw.text((w,h),str1,font=font,fill='#D4AF37')

    img.show()
    #img.save('{}.png'.format(j))  # uncomment this line to the left if you want to save the generated image files here




