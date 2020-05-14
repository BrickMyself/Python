def create_text(filename):
    path = 'C:/file1/'
    file_path = path + filename + '.txt'
    file = open(file_path, 'w')
    file.write("秦时明月汉时关，\n秦时明月汉时关。\n但使龙城飞将在，\n不教胡马度阴山。\n")
    file.close()
    f = open(file_path, 'r+')
    flist = f.readlines()
    flist[1] = '万里长征人未还\n'
    f = open(file_path, 'w+')
    f.writelines(flist)



#create_text('Py7-1')
from openpyxl import Workbook
def WriteData():
    # 创建一个Workbook对象
    wb = Workbook()
    # 获取当前活跃的sheet，默认是第一个sheet
    ws = wb.active

    row1 = ['S09','女','89.2','88.4','86','87.9']
    row2 = ['S10','女','90.5','86.3','87','87.9']
    row3 = ['S11','男','88.7','89.4','89','89.0']
    ws.append(row1)
    ws.append(row2)
    ws.append(row3)
    wb.save('ex06.xlsx')


WriteData()