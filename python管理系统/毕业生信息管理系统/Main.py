def Menu():  ##菜单主界面
    print('*' * 22)
    print("* 查看毕业生列表输入: 1 *")
    print("* 添加毕业生信息输入: 2 *")
    print("* 修改毕业生信息输入: 3 *")
    print("* 删除毕业生信息输入: 4 *")
    print("* 退出系统请输入     0 *")
    print('*' * 22)


def CheckIdisRight(StudentList, id):  ##检查学号是否在列表中
    for i in range(0, len(StudentList)):
        if ((id in StudentList[i]) == True):
            return True
    return False


def PrintStudentList(StudentList):  # 打印学生信息列表
    for i in range(0, len(StudentList)):
        print(StudentList[i])


def AddStudent(StudentList):  ##添加学生信息
    number = int((input("请输入学号： ")))
    if (number < 1000000000 and CheckIdisRight(StudentList, number) == False):  ##学号判断
        print("学号输入错误&学号已存在！请重新输入：")
        number = (input("请输入学号： "))
    name = input("请输入你的名字：")
    tell = input("请输入你的电话：")
    if (len(tell) != 11):
        print("请输入正确的电话号码(11)位： ")
        tell = input()
    college = input("请输入你的学院名称：")
    grade = input("请输入你的年级：")
    isjob = int(input("是否就业？：是填 1 否则填0: "))
    if (isjob == 1):
        company = input("请输入你公司的名称：")
    else:
        company = 0
    arry = [number, name, tell, college, grade, isjob, company]
    StudentList.append(arry)  ##将新建的学生信息进行插入
    PrintStudentList(StudentList)  ##打印学生信息列表


def StudentPersonalMsg():  ##修改信息界面选择
    print('*' * 22)
    print("* 修改姓名请输入: 1 *")
    print("* 修改电话号码请输入: 2 *")
    print("* 修改是否就业请输入: 3 *")
    print("* 修改就业公司请输入: 4 *")
    print("* 退出修改请输入： 0 *")
    print('*' * 22)


def ChangeStudent(StudentList):  ##修改学生信息模块
    ##默认学号 年级 等信息不可修改
    def changename(StudentList, arry, i):  # 修改姓名
        print(arry)
        name = input("请输入修改后的名字：")
        StudentList[i][1] = name
        print("修改后为：")
        PrintStudentList(StudentList)

    def changetell(StudentList, arry, i):  # 修改电话号码
        print(arry)
        tell = input("请输入修改后的电话号码：")
        StudentList[i][2] = tell
        print("修改后为：")
        PrintStudentList(StudentList)

    def changeisgob(StudentList, arry, i):  # 修改是否就业情况
        print(arry)
        isgob = int(input("请输入修改后的 是否工作："))
        StudentList[i][5] = isgob
        print("修改后为：")
        PrintStudentList(StudentList)

    def changcompany(StudentList, arry, i):  # 修改就业公司信息
        print(arry)
        company = input("请输入修改后的公司为：")
        StudentList[i][6] = company
        print("修改后为：")
        PrintStudentList(StudentList)

    print("请输入要修改的学生的学号：")
    id = int(input())
    i = 1
    if ((CheckIdisRight(StudentList, id)) == False):  ##判断学号是否存在
        print("学号不存在！")
    if (CheckIdisRight(StudentList, id) == True):
        while (i < len(StudentList)):  # 通过循环找到该学生的信息列表
            if (StudentList[i][0] == id):
                StudentPersonalMsg()  ##显示出修改的菜单选项
                while (1):
                    a = int(input("请输入： "))
                    while (a):
                        if (a == 1):
                            ##姓名修改
                            changename(StudentList, StudentList[i], i)
                            break
                        if (a == 2):
                            ##电话号码修改
                            changetell(StudentList, StudentList[i], i)
                            break
                        if (a == 3):
                            ##是否就业状态修改
                            changeisgob(StudentList, StudentList[i], i)
                            break
                        if (a == 4 and StudentList[i][5] == 1):
                            ##就业公司修改
                            changcompany(StudentList, StudentList[i], i)
                            break
                        if (a == 4 and StudentList[i][5] == 0):
                            print("学生尚未就业，请先修改是否就业信息！")
                            break
                    if (a == 0):
                        ##按0 退出修改信息功能
                        break
                ##返回到主界面的菜单选项
                break
            i = i + 1


def DeleteStudent(StudentList):  ##删除学生信息
    print("请输入要删除的学生的学号：输入0退出！")
    id = int(input())
    i = 1
    if (CheckIdisRight(StudentList, id) == False):
        print("学号不存在！")
    if (CheckIdisRight(StudentList, id) == True):
        ##同样先判断学号学号是否存在
        while (i < len(StudentList)):
            if (StudentList[i][0] == id):
                del StudentList[i]
                print("删除成功！")
                break
            if (id == 0):
                break
            i = i + 1
    PrintStudentList(StudentList)  # 打印学生信息列表


def main():
    Menu()
    StudentInfo = ['学号', '姓名', '电话', '学院', '年级', '是否就业', "就业公司"]
    ##先默认插入一个用于显示的列表的列表
    StudentList = [StudentInfo]
    while (1):
        a = int(input("请输入： "))
        while (a):

            if (a == 1):
                PrintStudentList(StudentList)
                Menu()
                break
            if (a == 2):
                AddStudent(StudentList)
                Menu()
                break
            if (a == 3):
                ChangeStudent(StudentList)
                Menu()
                break
            if (a == 4):
                DeleteStudent(StudentList)
                Menu()
                break
        if (a == 0):  ##按0退出进程
            exit()


main()
