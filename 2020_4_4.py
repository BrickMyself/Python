def String():
    s=input("请输入一个字符串：")
    result = []
    for i in s:
        result.append(ord(i))

    print("字符串的ASCII为：",result)
def Test1():
    def word_len(s):
        return len([i for i in s.split(' ') if i])

    def main():
        s = str(input("请输入字符串："))
        l = word_len(s)
        print("单词个数为：", l)

    main()
#Test1()
def Test2():
    s = input('请输入一个字符串:')
    letters = 0
    space = 0
    digit = 0
    others = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('英文字母：%d 个,空格：%d 个,数字：%d 个,其他字符：%d 个' % (letters, space, digit, others))
#Test2()
def Test3():
    counter = 0
    print("参考运行结果如下：")
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and k != i:

                 if (counter % 6) == 0:
                    print("\n")

            print("{}{}{}".format(i, j, k), end=" , ")
            counter += 1
Test3()