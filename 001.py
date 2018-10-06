#!/usr/bin/python3
import sys
import time
class Solution(object):
    def FibonacciD(self,n):
        if(n<=1):
            return n
        else:
            return (self.FibonacciD(n-1)+self.FibonacciD(n-2))
    def FibonacciF(self,n):
        if(n<=1):
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
def main():
    t1= time.clock()
    a = Solution()
    #print("请输入您想看到的位数")
    #for i in range(10000):
    #    if(a.FibonacciD(i-1)<sys.maxsize and a.FibonacciD(i)>sys.maxsize):
    #        print(i-1)
    for i in range(10000):
        if(a.FibonacciF(i-1)<sys.maxsize and a.FibonacciF(i)>sys.maxsize):
            print(i-1)
    # long running
    # do something other
    t2=time.clock()
    t3 = t2 -t1
    print(t3)
main()
