
###-----coding=utf-8
 
###----------------------------------------------------------------数据库
import pymssql
# ------打开数据库连接
db = pymssql.connect('.', database='BlogDB')
# -----使用cursor()方法获取操作游标
cursor = db.cursor()
# -------使用execute方法执行SQL语句
cursor.execute("select top 10 * from [BlogDB].[dbo].[Course]")
#----使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
#------fetchall()方法获取所有的数据
data2=cursor.fetchall()
length=len(data2)
for i in range(length):
    print(data2[i])

# # # # # sql="select top 10 * from [BlogDB].[dbo].[Course]"
# # # # # try:
# # # # #     cursor.execute(sql)
# # # # #     db.commit()
# # # # # except:
# # # # #     db.rollback()

#print (data)
#print(data2)
#---提交事务
db.commit()
#---关闭游标
cursor.close()
# ------关闭数据库连接
db.close()



###-------------------------------------------------------------2.excel 和csv文件
#导入csv
import csv
# 打开rent.csv文件
csv_file = open("rent.csv","w")
# 创建writer对象，指定文件与分隔符
csv_writer = csv.writer(csv_file, delimiter=',')
# 写一行数据
csv_writer.writerow("[house_title, house_location, house_money, house_url]")
#关闭文件
csv_file.close()

###-------------------------------------Excek 读取----------
import xlrd
 

# 设置路径
path = 'D:\Python\Crawer\project\input.xlsx'
# 打开execl
workbook = xlrd.open_workbook(path)

# 输出Excel文件中所有sheet的名字
print(workbook.sheet_names())

# 根据sheet索引或者名称获取sheet内容
Data_sheet = workbook.sheets()[0]  # 通过索引获取
# Data_sheet = workbook.sheet_by_index(0)  # 通过索引获取
# Data_sheet = workbook.sheet_by_name(u'名称')  # 通过名称获取


print(Data_sheet.name)  # 获取sheet名称
rowNum = Data_sheet.nrows  # sheet行数
colNum = Data_sheet.ncols  # sheet列数

# 获取所有单元格的内容
list = []
for i in range(rowNum):
    rowlist = []
    for j in range(colNum):
        rowlist.append(Data_sheet.cell_value(i, j))
    list.append(rowlist)
# 输出所有单元格的内容
for i in range(rowNum):
    for j in range(colNum):
        print(list[i][j], '\t\t', end="")
    print()

# 获取整行和整列的值（列表）
rows = Data_sheet.row_values(0)  # 获取第一行内容
cols = Data_sheet.col_values(1)  # 获取第二列内容
print (rows)
print (cols)

# 获取单元格内容
cell_A1 = Data_sheet.cell(0, 0).value
cell_B1 = Data_sheet.row(0)[1].value  # 使用行索引
cell_C1 = Data_sheet.cell(0, 2).value
cell_D2 = Data_sheet.col(3)[1].value  # 使用列索引
print(cell_A1, cell_B1, cell_C1, cell_D2)

# 获取单元格内容的数据类型
# ctype:0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print('cell(0,0)数据类型:', Data_sheet.cell(0, 0).ctype)
print('cell(1,0)数据类型:', Data_sheet.cell(1, 0).ctype)
print('cell(1,1)数据类型:', Data_sheet.cell(1, 1).ctype)
print('cell(1,2)数据类型:', Data_sheet.cell(1, 2).ctype)

# 获取单元格内容为日期的数据
date_value = xlrd.xldate_as_tuple(Data_sheet.cell_value(1,0),workbook.datemode)
print(type(date_value), date_value)
print('%d:%d:%d' % (date_value[0:3]))

#------------------------------------------写入Excel--------
import xlwt

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style

def write_excel(path):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo')
    row0 = [u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID']
    row1 = [u'测试', '15:50:33-15:52:14', 22706, 4190202]
    # 生成第一行和第二行
    for i in range(len(row0)):
data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))

    # 保存文件
    # workbook.save('demo.xls')
    workbook.save(path)

if __name__ == '__main__':
    # 设置路径
    path = 'D:/demo.xlsx'
    write_excel(path)
    print(u'创建demo.xls文件成功')
#--------------------------------------------------------3.csv文件

import csv

##------读取csv
with open('tr.csv','r',encoding="ascii",errors="surrogateescape")as csvfile:
    readCSV=csv.reader(csvfile)
    for row in readCSV:
        print(row)
#-------------------------------------------------------写入csv

import csv
with open('tr.csv','w',encoding="ascii",errors="surrogateescape")as csvfile:
    csvwriter=csv.writer(csvfile,dialect=("excel"))
    csvwriter.writerow(["1","b"])

#---------------------------------------------------------3.json文件

import json

with open('Jon.json', 'r',encoding='utf-8') as f:
    data = json.load(f)
# 格式化显示读取文件内容
a = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
print(a)
# 修改
data['SidebarExpandedItems'] = '文件状态修改','分支修改','添加修改'
# 添加/增加
data['新添加的键'] = '新添加的值'
# 删除
del data['$id']
# 写入文件，并格式化输出
with open('Jon_new.json', 'w',encoding='utf-8') as f:
    json.dump(data, f, sort_keys=True, indent=4,ensure_ascii=False)

#--=-------------------------------------------------------4.xml 文件

import xml.etree.ElementTree as ET

tree = ET.parse('XML.xml')

root = tree.getroot()

print(root.tag)

# 一个节点有tag、attrib、text三个值

# tag是标签的名字

# text是标签的内容

# attrib是标签属性的字典，通过字典的get('key')来获取对应的属性的值


# 直接for chile in parent 来遍历节点下的子节点

for child in root:

    print(child.tag, child.attrib)

    for elem in child:

        print(elem.tag, elem.text, elem.attrib)
# 只遍历year节点

for node in root.iter('branch'):

    print(node.tag, node.text)