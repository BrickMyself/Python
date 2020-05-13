def test1():
    s1=input("请输入一个字符串：")
    i=0
    count=0
    for i in range(0,len(s1)):
        if(s1[i]=='A' or s1[i]=='E' or s1[i]=='I' or s1[i]=='O' or s1[i]=='U' or s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u'):
            count+=1
    print(str(count))
#test1()
def test2():
    x = ["13915556234", "13025621456", "15325645124", "15202362459"]
    for i in range(0,len(x)):
        s=x[i]
        if(s[0]=='1' and s[1]=='3'):
            if(s[2]=='4' or s[2]=='5' or s[2]=='6' or s[2]=='7' or s[2]=='8' or s[2]=='9' ):
                print(s+"是移动号码")
        if(s[0]=='1' and s[1]=='5'):
            if(s[2]=='0' or s[2]=='1' or s[2]=='2' or s[2]=='8' or s[2]=='9' ):
                print(s+"是移动号码")
test2()
