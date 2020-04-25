#输入一个字符串，将该字符串中下标为偶数的字符组成新串并通过字符串格式化 方式显示。
def test1():
    s1=input("请输入一个字符串：")
    s2=s1[0:len(s1):2]
    print(s2)
#test1()
#编写程序，生成一个 15 个不重复的大小写字母组成的列表。
import random
def test2():
    str1='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM'
    str2=random.sample(str1,15)
    print(str2)
test2()
#给定字符串"site seasuede sweetseekasessesseeloses"，匹配出所有 s 开头，e 结 尾的单词。
import re
def test3():
    str1="site seasuede sweetseekasessesseeloses"
    str2=re.compile(r'\bs\S*?e\b')
    print(re.findall(str2,str1))
#test3()
#生成 15 个包括 10 个字符的随机密码，
# 密码中的字符只能是大小写字母、数字和 特殊字符“@”、“$”、“#”、“&”、“_”、“~”构成。
def test4():
    str='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890@$#&_~'
    for i in range(0,15):
        str2 = random.sample(str, 10)
        print(str2)
#test4()


