#!/usr/bin/python3
import sys
import time
class Solution(object):
    k =("--------------------------------------------------\n"
        "您需求计算机所能表示的最大整数还是自选位数Fibonacci数:\n"
        "---------------(1)最大整数及所用时间--------------\n"
        "---------------(2)选定位数及所用时间--------------\n"
        "---------------(q)退出----------------------------")
    l = ("-------------------------------------------------\n"
         "----------------(1)返回主菜单--------------------\n"
         "----------------(2)返回当前页面------------------\n"
         "----------------(q)直接退出----------------------")
    def FibonacciD(self,n):
        if(n<=1):
            return n
        else:
            return (self.FibonacciD(n-1)+self.FibonacciD(n-2))
    def FibonacciF(self,n):
        if(n==1):
            return n
        if(n ==2):
            return 1
        else:
            a = 1
            b = 1
            for i in range(n-2):
                sum = a + b
                b   = a
                a   = sum
            return sum
    def FibonacciOF(self,n):
            list = [1, 1]
            if n > 2:
                for i in range(2, n, 1):
                    listNew = list[i - 2] + list[i - 1]
                    list.append(listNew)
            return list[n - 1]
    def return_Old_Fib(self):
        r = (input("请输入您的选择:"))
        if r == "1":
            main()
        elif r == "2":
            self.Old_Time_Fib()
        elif r =="q":
            exit("程序结束")
        else:
            print("不符合输入规则，请重新输入")
            self.Old_Time_Fib()
    def return_New_Fib(self):
        r = (input("请输入您的选择:"))
        if r == "1":
            main()
        elif r == "2":
            self.New_Time_Fib()
        elif r =="q":
            exit("程序结束")
        else:
            print("不符合输入规则，请重新输入")
            self.New_Time_Fib()
    def return_interation(self):
        r = (input("请输入您的选择:"))
        if r == "1":
            main()
        elif r == "2":
            self.Time_interation()
        elif r =="q":
            exit("程序结束")
        else:
            print("不符合输入规则，请重新输入")
            self.Time_interation()
    def New_Time_Fib(self):
        print("-------------------迭代法-------------------------")
        print(self.k)
        r=(input("请输入您的选择:"))
        if (r !="q"):
            if(r == "1"):
                i = 1
                while self.FibonacciF(i) <= sys.maxsize:
                    i = i + 1
                else:
                    t1 = time.clock()
                    print("计算机能表示最大整数对应的位数为:",i - 1)
                    t2 = time.clock()
                    t3 = t2 - t1
                    print("执行时间为:", t3)
            elif (r =="2"):
                o = int(input("请输入你选定的位数:"))
                if (o>=0):
                    t1 = time.clock()
                    print("该位数的Fibonacci数为:", self.FibonacciF(o))
                    t2 = time.clock()
                    t3 = t2 - t1
                    print("执行时间为:", t3)
                else:
                    print("输入错误，请重新输入")
            else:
                print("不符合输入规则，请重新输入")
                self.New_Time_Fib()
        print(self.l)
        self.return_New_Fib()
    def Old_Time_Fib(self):
        print("-----------------旧迭代法-------------------------")
        print(self.k)
        r=(input("请输入您的选择:"))
        if (r !="q"):
            if r == "1":
                i = 1
                while self.FibonacciOF(i) <= sys.maxsize:
                    i = i + 1
                else:
                    t1 = time.clock()
                    print("计算机能表示最大整数对应的位数为:",i - 1)
                    t2 = time.clock()
                    t3 = t2 - t1
                    print("执行时间为:", t3)
            elif r =="2":
                o = int(input("请输入你选定的位数:"))
                if (o>=0):
                    t1 = time.clock()
                    print("该位数的Fibonacci数为:", self.FibonacciOF(o))
                    t2 = time.clock()
                    t3 = t2 - t1
                    print("执行时间为:", t3)
                else:
                    print("输入错误，请重新输入")
            else:
                print("不符合输入规则，请重新输入")
                self.Old_Time_Fib()
        print(self.l)
        self.return_Old_Fib()
    def Time_interation(self):
        print("-------------------递归法-------------------------")
        print(self.k)
        r=(input("请输入您的选择:"))
        if (r !="q"):
            if r == "1":
                i = 1
                while self.FibonacciD(i)<=sys.maxsize:
                    i = i + 1
                else:
                    t1 = time.clock()
                    print("计算机能表示最大整数对应的位数为:", i - 1)
                    t2 = time.clock()
                    t3 = t2 - t1
                    print("执行时间为:", t3)
            elif r =="2":
                o=int(input("请输入你选定的位数:"))
                t1 = time.clock()
                print("该位数的Fibonacci数为:",self.FibonacciD(o))
                t2 = time.clock()
                t3 = t2 - t1
                print("执行时间为:", t3)
            else:
                print("不符合输入规则，请重新输入")
        print(self.l)
        self.return_interation()
def main():
    a = Solution()
    print("---------------------------------------\n"
          "-----------Fibonacci_numbers-----------\n"
          "-------------(1)迭代方法求解-----------\n"
          "-------------(2)递归算法求解-----------\n"
          "-------------(3)优化迭代方法求解-------\n"
          "-------------(q)退出-------------------\n"
          "------------请选择您需要的方法---------")
    j = (input("请输入您的选择:"))
    if(j == "1"):
        a.Old_Time_Fib()
    elif(j=="2"):
        a.Time_interation()
    elif(j=="3"):
        a.New_Time_Fib()
    elif(j=="q"):
        exit("程序结束")
main()
