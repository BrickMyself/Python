StudentInfo = ['学号', '姓名', '性别', '毕业年级', '就业公司名称', '电话号码(+86)', '家庭住址']


def GetList():  # 将 StudentMsg.txt 中的数据 拷贝到一个列表中
    fiel = open('StudentMsg.txt', 'r', encoding='utf-8')
    l = []
    for line in fiel:
        l.append(line.strip())
    return l


def PrintAllMsg():  # 打印出所有的信息
    l = GetList()
    print(StudentInfo)
    count = 0
    for i in range(0, len(l)):
        count = count +1
        print(l[i], end="     ")
        if count % 7 == 0:
            print()
    print()


def ModifyMenu():
    print('-' * 22)
    print("# 修改姓名请输入:     1 *")
    print("# 修改性别请输入:     2 *")
    print("# 修改毕业年级请输入: 3 *")
    print("# 修改公司信息请输入: 4 *")
    print("# 修改电话号码请输入: 5 *")
    print("# 修改家庭住址请输入: 6 *")
    print("# 退出修改请输入： 0 *")
    print('-' * 22)


def ModifyMsg():
    def ModifyName(pos):
        f = open('StudentMsg.txt','r+', encoding='utf-8')
        flist = f.readlines()
        name = input("输入修改之后的姓名：")
        name += '\n'
        flist[pos+1] = name
        f = open('StudentMsg.txt', 'w+', encoding='utf-8')
        f.writelines(flist)
        f.close()
        print("修改成功！")

    def ModifySex(pos):
        Sex = ['男', '女']
        f = open('StudentMsg.txt', 'r+', encoding='utf-8')
        flist = f.readlines()
        sex = input("输入修改之后的性别：")
        if sex in Sex:
            sex += '\n'
            flist[pos + 2] = sex
            f = open('StudentMsg.txt', 'w+', encoding='utf-8')
            f.writelines(flist)
            f.close()
            print("修改成功！")
        else:
            print("输入错误！")
            print("修改失败！")
            ModifySex(pos)

    def ModifyYear(pos):
        f = open('StudentMsg.txt', 'r+', encoding='utf-8')
        flist = f.readlines()
        year = input("输入修改之后的年级：")
        if int(year)>2000:
            year += '\n'
            flist[pos+3] = year
            f = open('StudentMsg.txt', 'w+', encoding='utf-8')
            f.writelines(flist)
            f.close()
            print("修改成功！")
        else:
            print("输入错误！")
            print("修改失败！")
            ModifyYear(pos)

    def Modifycompany(pos):
        f = open('StudentMsg.txt','r+', encoding='utf-8')
        flist = f.readlines()
        company = input("输入修改之后的公司：")
        company+='\n'
        flist[pos+4] = company
        f = open('StudentMsg.txt', 'w+',encoding='utf-8')
        f.writelines(flist)
        f.close()
        print("修改成功！")

    def ModifyTell(pos):
        f = open('StudentMsg.txt','r+', encoding='utf-8')
        flist = f.readlines()
        tell = input("输入修改之后的电话号码：")
        if len(tell) == 11:
            tell += '\n'
            flist[pos + 5] = tell
            f = open('StudentMsg.txt', 'w+', encoding='utf-8')
            f.writelines(flist)
            f.close()
            print("修改成功！")
        else:
            print("输入错误！")
            print("修改失败！")
            ModifyTell(pos)

    def ModifyAddress(pos):
        f = open('StudentMsg.txt','r+', encoding='utf-8')
        flist = f.readlines()
        address = input("输入修改之后的地址：")
        address+='\n'
        flist[pos+6] = address
        f = open('StudentMsg.txt', 'w+',encoding='utf-8')
        f.writelines(flist)
        f.close()
        print("修改成功！")
    PrintAllMsg()
    id = input("请输入你要修改的学号：")
    if id in IsIdRight():
        l2 = GetList()
        pos = l2.index(id)
        while 1:
            ModifyMenu()
            a = int(input("请输入： "))
            while a:
                if a == 1:
                    ModifyName(pos)
                    break
                if a == 2:
                    ModifySex(pos)
                    break
                if a == 3:
                    ModifyYear(pos)
                    break
                if a == 4:
                    Modifycompany(pos)
                    break
                if a == 5:
                    ModifyTell(pos)
                    break
                if a == 6:
                    ModifyAddress(pos)
                    break
            if a == 0:  # 按0退出进程
                break


def DelMsg():
    PrintAllMsg()
    id = input("请输入你要删除的学生的Id:")
    if id in IsIdRight():
        pos = GetList().index(id)
        f = open('StudentMsg.txt','r+', encoding='utf-8')
        flist = f.readlines()
        for i in range(0, 7):
            del flist[pos]
        f = open('StudentMsg.txt', 'w+', encoding='utf-8')
        f.writelines(flist)
        f.close()
        print("删除成功！")
        PrintAllMsg()
    else:
        print("学号输入错误！")
        DelMsg()


def IsIdRight():  # 返回学号列表
    l1 = GetList()
    l2 = []
    i = 0
    while i <len(l1):
        l2.append(l1[i])
        i = i+7
    return l2


def AddMsg():  # 添加信息
    fiel = open('StudentMsg.txt', 'a', encoding='utf-8')

    def Inputid():  # 添加学号判断
        id = (input("请输入你的学号："))
        l1 = IsIdRight()
        if (int(id) > 1000 and ((id in l1) == False)):
            fiel.write('\n')
            fiel.writelines(id)
        else:
            if int(id) <1000:
                print("学号输入错误！")
                Inputid()
            if id in IsIdRight():
                print("学号存在！")
                Inputid()


    def Inputname():  # 添加姓名判断
        name = input("请输入你的姓名：")
        fiel.write('\n')
        fiel.writelines(name)

    def InputSex():  # 添加性别判断
        sex = ['男', '女']
        s1 = input("请输入你的性别")
        if s1 in sex:
            fiel.write('\n')
            fiel.writelines(s1)
        else:
            print("性别输入错误！")
            InputSex()

    def InputGaduYear():  # 添加毕业年级判断
        year = (input("请输入你的毕业年级："))
        if int(year)>2000:
            fiel.write('\n')
            fiel.writelines(year)
        else:
            print("毕业年级输入错误！")
            InputGaduYear()

    def InputCompany():  # 添加公司信息
        company = input("请输入你的就业公司：")
        fiel.write('\n')
        fiel.writelines(company)

    def InputTell():  # 添加电话判断
        tell = (input("请输入你的电话号码："))
        if len(tell) == 11:
            fiel.write('\n')
            fiel.writelines(tell)
        else:
            print("电话号码输入错误！")
            InputTell()

    def InputAddress():  # 添加地址信息
        add = input("请输入你的家庭地址：")
        fiel.write('\n')
        fiel.writelines(add)
    Inputid()
    Inputname()
    InputSex()
    InputGaduYear()
    InputCompany()
    InputTell()
    InputAddress()
    fiel.close()  # 关闭文件


def Menu():  # 菜单主界面
    print('-' * 22)
    print("# 查看毕业生列表输入: 1 *")
    print("# 添加毕业生信息输入: 2 *")
    print("# 修改毕业生信息输入: 3 *")
    print("# 查找毕业生信息输入：4 *")
    print("# 删除毕业生信息输入: 5 *")
    print("# 退出系统请输入      0 *")
    print('-' * 22)


def FindMenu():
    print('-' * 22)
    print("# 搜索学号请输入: 1 *")
    print("# 搜索姓名请输入: 2 *")
    print("# 退出搜所请输入  0 *")
    print('-' * 22)


def FindStu():
    def FindMsgById():
        id = input("请输入你需要查找的学生的学号：")
        if id in IsIdRight():
            pos = GetList().index(id)
            flist = GetList()
            print(StudentInfo)
            for i in range(0, 7):
                print(flist[pos + i], end="     ")
            print()
        else:
            print("学号输入错误！")
            FindMsgById()

    def FindMsgByName():
        name = input("请输入你需要查找的学生的姓名：")
        if name in GetList():
            pos = GetList().index(name)-1
            flist = GetList()
            print(StudentInfo)
            for i in range(0, 7):
                print(flist[pos + i], end="     ")
            print()
        else:
            print("姓名输入错误！")
            FindMsgByName()
    while 1:
        FindMenu()
        a = int(input("请输入： "))
        while a:
            if a == 1:
                FindMsgById()
                break
            if a == 2:
                FindMsgByName()
                break
        if a == 0:
            break


def main():
    Menu()
    while 1:
        a = int(input("请输入： "))
        while a:

            if a == 1:
                PrintAllMsg()
                Menu()
                break
            if a == 2:
                AddMsg()
                Menu()
                break
            if a == 3:
                ModifyMsg()
                Menu()
                break
            if a == 4:
                FindStu()
                Menu()
                break
            if a == 5:
                DelMsg()
                Menu()
                break
        if a == 0:  # 按0退出进程
            exit()


main()
