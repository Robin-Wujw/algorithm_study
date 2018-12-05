#!/usr/bin/python3
import sys
import math
def DP(n):
    A = []
    if len(n)==0:
        return 0
    A.append(n[0])
    Amax = A[0]
    #求单段最大值的方法
    for i in range(1,len(n)):
        if A[i-1]>0:
            A.append(A[i-1]+n[i])
        else:
            A.append(n[i])
        if A[i-1] >=Amax:
            Amax = A[i]
    return Amax
def MAXL(n):
    MAX = 0
    #循环求出所有可能情况的最大值
    for i in range(len(n)):
        if MAX < DP(n[0:i])+DP(n[i:]):
            MAX = DP(n[0:i])+DP(n[i:])
    return MAX
def main():
    list=input("请输入一列数组,用逗号分开:")
    n=[int(n) for n in list.split(",")]
    print("不相交的两个字段和最大为:",MAXL(n))
main()