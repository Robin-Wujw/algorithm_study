#! /usr/bin/python3
class Solution():
    def First(self,x,n):
        b = x
        if (n<=0):
            return 1
        else:
            for i in range(n-1):
                x = x * b
        return x
    def Second(self,x,n):
         if n <=0:
             return 1
         x = x * self.Second(x,n-1)
         return x
    def Third(self,x,n):
        b = x
        if n <=0:
            return 1
        else:
            if n % 2 == 0:
                return self.Third(x,n/2)*self.Third(x,n/2)
            else:
                return self.Third(x,(n-1)/2) * self.Third(x,(n-1)/2) * x
    def Four(self,x,n):
        b = x
        if n <=0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            x = self.Four(x,n/2)
            x = x * x
        else:
            x = self.Four(x,(n-1)/2)   
            x = x * x * b
        return x

def main():
    a = Solution()
    x = int(input("请输入底数："))
    n = int(input("请输入指数："))
    print(a.First(x,n))
    print(a.Second(x, n))
    print(a.Third(x, n))
    print(a.Four(x, n))
main()
