from turtle import *

def Test1():#画一个三角形
  forward(100)
  left(120)
  forward(100)
  left(120)
  forward(100)
  pendown()
#Test1()
def Test2():
    print('C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
    print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')##保持字符串的原样进行输出 忽略转义字符\
#Test2()
def Test3():
    print(10//-3)#在python 有一种对商做向下圆整的方式 比如 10 除以 -3 应该等于 -3 但是打印结果是 -4 因为 -4 是小于-3 的
    #是一种向下的 10 //3 也是 本来应该是 3.333但是当要去一个整数的时候 取了3 因此这是一种向下圆整的方式
    print(10//3)
    print("Today I found a lonely kitten: \N{Cat}")
#Test3()


def Test4():
    print()
    print("Today I found a lonely kitten: \N{Cat}")


Test4()
##列表和元组 两种容器主要的容器 （序列：如列表 元组 映射 ： 如字典）
### 序列里面的元素都可以使用编号来访问
###列表：
def TestList():
    first = ["小李", 30]
    second = ["小明", 40]
    database = [first, second]
    print(database)
    print(database[1])
    print(database[-2])#当是负数的编号为 -1 时 会从索引的最右边开始访问  但是负数的绝对值超过容器的大小时会出现越界
    str = "helloworld"
    print(str[-4])#python中没有专门的string 相关的容器
    #Python没有专门用于表示字符的类型，因此一个字符就是只包含一个元素的字 符串。
    ##切片 用于提取序列中的一部分内容 每次增加一个元素
    str="Today i found a lonely kitten: \N{cat} "
    print(str[5:-1])
    print(str[5:])#编号5后面所有的
    print(str[:-1])#除了最后一个
    print(str[:])#整个序列
    ## 当要一次跳过一个，即一次走两步的取一个数
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(arr[0:10:2])#步长为 2 但是步长不能为 0 但是可以为负数 即从右向左的取数据
    print(arr[1:10:2])#[2, 4, 6, 8, 10]
    print(arr[10:0:-2])#[10, 8, 6, 4, 2]
    ##序列的相加
    str1 = "hello"
    str2 = " world"
    arr1 = [1, 2, 3]
    arr2 = [2, 4, 6]
    arr3 = arr1+arr2
    print(arr3)
    print(str1+str2)
    #print(str1+arr1) 但是不同类型的不能相加
    ## 乘法
    str5 = "hello"
    print(str5*5)#hellohellohellohellohello
    arr = [10]
    print(arr*10)#[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    ## None、空列表和初始化
    q=[None]
    print(q*10)#[None, None, None, None, None, None, None, None, None, None]


TestList()