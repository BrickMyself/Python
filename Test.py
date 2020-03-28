def SanjiaoXingArea():
    a = float(input("请输入三角形的边长："))
    b = float(input("请输入三角形的边长："))
    c = float(input("请输入三角形的边长："))
    print("三角形的三边分别为：""a=" + str(a) + "," + "b=" + str(b) + "," + "c=" + str(c))
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("三角形的面积= " + str(area))
    else:
        print("输入错误")


def GradeMatch():
    mark = int(input("请输入成绩"))
    if 100 >= mark >= 90:
        print("优")
    elif 90 > mark >= 80:
        print("良好")
    elif 80 > mark >= 70:
        print("中")
    elif 70 > mark >= 60:
        print("及格")
    else:
        print("不及格")


def GetPayTaxes():
    x = int(input("请输入工资： "))
    y=float
    if 5000 > x >= 0:
        y = 0
    elif 36000 >= x > 5000:
        y = float((x - 5000) *0.03)
    elif 144000 >= x > 36000:
        y = float(((x - 5000) * 0.1) - 2520)
    elif x > 144000:
        y = float(((x - 5000) * 0.2) - 16920)
    round(y,6)
    print("应交税款为： " + str(y))
GetPayTaxes()


def ChessWhichWeek():
    str = input("请输入字母：")
    if str == 'M' or str == 'm':
        print("星期一")
    elif str == 'T' or str == 't':
        str1 = input(("请输入第二个字母："))
        if str1 == 'U' or str1 == 'u':
            print("星期二")
        elif str1 == 'H' or str1 == 'h':
            print("星期四")
    elif str == 'W' or str == 'w':
        print("星期三")
    elif str == 'F' or str == 'f':
        print("星期五")
    elif str == 'S' or str == 's':
        str2 = input("请输入第二个字母： ")
        if str2 == 'A' or str2 == 'a':
            print("星期六")
        if str2 == 'U' or str2 == 'u':
            print("星期日")
    else:
        print("输入错误")
