def test1():
    arry=[10,23,35,46,57,68,79,80,92,103]
    a=int(input("请输入要插入的数字："))
    for i in range(0,len(arry)):
        if(arry[i]>a):
            arry.insert(i, a)
            break
    print(arry)
#test1()
def test2():
    a=input("请输入一个5位数字：")
    if(a[0]==a[4] and a[1]==a[3]):
        print("这是一个回文数字")
    else:
        print("这不是一个回文")
#test2()
def test3():
    a=int(input("请输入一个正整数："))
    for i in range(2,a-1):
        if((a//i)==0):
            print(str(a)+"不是素数")
            break
        else:
            print(str(a)+"是素数")
            break
#test3()
def test4():
    total=100
    totalProduct=100
    big=3
    midle=2
    small=float(0.5)
    for i in range(0,34):
        for j in range(0,50):
            for k in range(0,101-i-j):
                if(((i+j+k)==total)and((i*big+j*midle+k*small)==totalProduct)):
                    print("大马有:"+str(i)+"匹"+"，"+"中马有:"+str(j)+"匹，"+"小马有:"+str(k)+"匹")
                else:
                    continue
test4()