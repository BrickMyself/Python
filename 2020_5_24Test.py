#任务一：设计一个 Circle 类来表示圆，
# 这个类包含圆的半径以及求面积和周长的函数。
# 再 使用这个类创建半径为 1~10 的圆，并计算出相应的面积和周长。
# 运行结果如下：
#半径为 1 的圆，面积： 3.14 周长： 6.28
# 半径为 2 的圆，面积： 12.57 周长： 12.57
# 半径为 3 的圆，面积： 28.27 周长： 18.85
# 半径为 4 的圆，面积： 50.27 周长： 25.13
# 半径为 5 的圆，面积： 78.54 周长： 31.42
# 半径为 6 的圆，面积： 113.10 周长： 37.70
# 半径为 7 的圆，面积： 153.94 周长： 43.98
# 半径为 8 的圆，面积： 201.06 周长： 50.27
# 半径为 9 的圆，面积： 254.47 周长： 56.55
# 半径为 10 的圆，面积： 314.16 周长： 62.83


#class Circle:
#    def __init__(self, r):

#        self.r = r

#    def printSquare(self):

#        print("半径为"+str(self.r)+"的圆，面积： "+'%.2f' %(3.1415*(self.r**2))+"周长： "+'%.2f' %(2*3.1415*self.r))


#for i in range(1, 11):
#    c = Circle(i)

   # c.printSquare()
#任务二：设计一个 Account 类表示账户，自行设计该类中的属性和方法，
#并利用这个类创 建一个账号为 998866，余额为 2000，
#年利率为 4.5%的账户，然后从该账户中存 入 150，取出 1500。
#打印出帐号、余额、年利率、月利率、月息。


class Account:
    def __init__(self, number, money):

        self.number = number

        self.money = money

    def storage(self, m):

        self.money = self.money+m
        print("存入" + '%d' %m + "元"+"你的余额为： " + '%d' % self.money)

    def get(self, m):

        self.money = self.money-m
        print("取出" + '%d' % m + "元"+"你的余额为： " + '%d' % self.money)

    def Print(self):

        year = str(0.045)
        month = str(0.00375)
        anthony = str(self.money*0.00375)
        print("您的账户： "+'%d' % self.number+" 的余额为： "+'%d' % self.money)
        print("年利率为： " + str(year)+"月利率为 ：" + str(month)+" 月息为：" + anthony)


person = Account(998866, 2000)
person.storage(150)
person.get(1500)
person.Print()





