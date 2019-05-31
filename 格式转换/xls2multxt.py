# 将xls文件的每一行保存到一个文本里
import xlrd

def strs(row):
    values = ""
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i]) + ","
    return values

# 打开文件
data = xlrd.open_workbook("e:/语料库/url爬虫/seed.xls")


table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(0)  # 某一行数据
# 打印出行数列数
#print(nrows)
#print(ncols)
#print(colnames)
list=[]
for ronum in range(1, nrows):
    row = table.row_values(ronum)
    values = strs(row) # 将行数据拼接成字符串
    list.append(values)
fw=open('e:/鹰眼/yn.txt','w')
for l in list:
    fw.writelines(l+"\n") #将字符串写入新文件
fw.close()
print("over!")