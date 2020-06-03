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


#Test4()
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
    ### 判断一个元素是否在这个序列中
    Student = ["张三", "李四", "王五", "毛六"]
    name = input("请输入你的名字： ")
    if(name in Student):#如果这个名字在序列中的话 返回 True 否则返回 False
        print("you are a student")
    else:
        print("you are not a student")
    ##长度、最小值和最大
    x = [123, 5, 678]
    print(len(x))#计算出其长度
    print(max(x))#计算出其中的最大值
    print(min(x))#计算出其最小值


#TestList()##类 list 列表
def studylist():
    l = list('hello world!')#定义一个存放 hello world! 的字符列表
    s = ''.join(l)##''.join(somelist) 将字符列表转换为 字符串
    print(l)#['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
    print(s)
    #基本的列表操作
    ## 1. 修改列表：给元素赋值
    l1 = [1, 2, 3, 4, 5, 6]
    l1[3]=8#将编号为 3的也就是第四个位置的元素的值更改为 8 [1, 2, 3, 8, 5, 6]
    ##但是不能给不存在的编号位置处进行修改元素
    print(l1)
    ## 2. 删除元素 del 语句
    del l1[4]#删除 编号为 4 也就是第五个位置的元素
    print(l1)##[1, 2, 3, 8, 6]
    ## 3. 给切片赋值 也就是我们理解的用一个 list的一个片段进行创建一个 变量
    l2 = list('hello')
    l2[2:] = list('world')
    print(l2)#['h', 'e', 'w', 'o', 'r', 'l', 'd']
    numbers = [1, 5]
    numbers[1:1] = [2, 3, 4]#numbers[1:1] 相当于一个空的 切片将这个空的一段替换也就是插入[2, 3, 4]
    print(numbers)#[1, 2, 3, 4, 5]
    ##相反的是假如将一段区间的元素置为空 那么就是删除掉这一段元素
    numbers[1:3]=[]
    print(numbers)#[1, 4, 5]
    ### 列表内的方法
    #### 1.append 尾加一个数据
    numbers.append(6)
    print(numbers)#[1, 4, 5, 6]
    #### 2.clear清空
    print(numbers)#什么也没有
    #### copy
    a = [1, 2, 3]
    b = a.copy()
    print(b)#[1, 2, 3]
    #### count 计算一个元素出现的次数
    y = b.count(2)
    print(y)#1
    #### 相当于将整个 列表 b 附加到 a 后面  返回的是被追加的列表  但是使用 + 的话会返回一个新的 列表
    a.extend(b)
    print(a)#[1, 2, 3, 1, 2, 3]
    #### 6. index 方法index在列表中查找指定值第一次出现的索引 当不存在的时候会报错
    knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
    temp = knights.index('who')
    print(temp)#4
    #### 7. insert 方法insert用于将一个对象插入列表。
    ##### objec.insert(pos,value)
    str1 = ["h", "e", "l", "o"]
    str1.insert(3, 'l')
    print(str1)#['h', 'e', 'l', 'l', 'o']
    #### 8. pop 方法pop从列表中删除一个元素（末尾为后一个元素），并返回这一元素
    ### python中没有 push 因此使用 pop 和 insert 或者 append 可以实现一个简单的 栈
    str1.pop()# l
    print(str1.pop())
    print(str1)#['h', 'e', 'l', 'l']
    #### 9. remove 方法remove用于删除第一个为指定值的元素。
    str2 = ['w', 'o', 'w', 'r', 'l', 'd']
    str2.remove('w')
    print(str2)#['o', 'w', 'r', 'l', 'd']
    #### 10. reverse 方法reverse按相反的顺序排列列表中的元素 修改列表但是不返回任何的值
    str2.reverse()
    print(str2)#['d', 'l', 'r', 'w', 'o']
    #### 11. sort 方法sort用于对列表就地排序①。
    #### 就地排序意味着对原来的列表进行修改，使其元素按顺序 排列，而不是返回排序后的列表的副本。
    arry = [1,5,7,342,43,37]
    #arry.sort()
    print(arry)##[1, 5, 7, 37, 43, 342]
    ###!!!! 注意上述的很多操作时没有返回值的 因此想要返回值的时候 可以先将其 使用 copy 出一个副本 对他的副本进行操作
    ## 再将其副本 返回即可如：
    arry2 = arry.copy()
    arry2.sort()
    print(arry2)## [1, 5, 7, 37, 43, 342]
    ### 但是直接赋值是不行的 比如 将 y = x这样 x y还是指向同一个列表 但是可以使用 sorted 如：
    arry3 = sorted(arry)
    print(arry)## [1, 5, 7, 342, 43, 37]
    print(arry3)##[1, 5, 7, 37, 43, 342]
    ### sorted 适合于所有的序列 返回的是一个列表
    #####12. 高级排序 方法sort接受两个可选参数：key和reverse
    arry4 = ["hr", "dka", "s", "sdgafkhl"]
    arry4.sort(key=len)
    print(arry4)##['s', 'hr', 'dka', 'sdgafkhl']
    arry5 = [-1, 0, 131, 34, 4]
    arry5.sort(reverse=True)##[131, 34, 4, 0, -1]
    print(arry5)
    # 2.4 元组：不可修改的序列
    ### 。元组语法很简单，只要将一些值用逗号分隔，就能自动创建一个元组。 >>>
    print(1, 2, 3)
    print(3*(1, 2, 3))##(1, 2, 3, 1, 2, 3, 1, 2, 3)
    ##tuple 它将一个序列作为参数，并将其转换为元组
    arr6 = [1, 4, 7, 9, 34]
    print(tuple(arr6))##(1, 4, 7, 9, 34)


studylist()
