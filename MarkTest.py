def Test1():
    l1 = [1, 2, 3, 4]
    l1[3] = 9
    print(l1)# 对序列中的索引位置的值进行修改
    print('hello'[3])# 直接打印出序列 'hello' 的索引为 3位置的值 无需再创建一个新的序列变量
    fourth = input("请输入： ")[3]##返回用户输入的第四个的值
    print(fourth)


#Test1()
def Test2():
    str1 = "hello world!"
    print(str1[1:6])


#Test2()
def Test3():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(a[1:-2])# 切片也同样支持负索引的操作 但是也要注意正负索引不要超出序列的范围
    print(a[-4:-1])#打印最后三个元素 可以使用负索引来解决 非常的方便 当然还有以下的一些更为简洁的操作
    print(a[-4:])#打印最后四个元素 这里 可以省略第二个索引
    print(a[:3])#打印前三个元素 这里可以省略第一个索引
    print(a[:])#打印出整个序列


#Test3()
def Test4():
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(b[0:10:2])
    print(b[1:10:2])
    print(b[0:10:3])


#Test4()
def Test5():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a+b
    print(c)


#Test5()
def Test6():
    a = []
    print(a)#一个空的序列
    b = [None]*10#使用 None 来初始化
    print(b)


#Test6()
def Test7():
    a = [1, 2, 3, 4, 5, 6]
    print(2 in a)
    print(0 in a)


#Test7()
def Test8():
    a = [1, 2, 'r', 4, 5]
    s = "hello world!"
    print(len(a))
    print(a[2])


#Test8()
def Test9():
    a = [1, 2, 3]
    a[1:2] = [4, 56, 9]
    print(a)

Test9()