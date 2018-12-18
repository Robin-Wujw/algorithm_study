#!/usr/bin/python3
import sys
def Quick_Sort(A,p,r):
    if p < r :
        q = Partition(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q+1,r)
    return A
def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <=x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
def main():
    a = []
    Len = int(input("请输入您想排序的数的个数:"))
    print("请输入您想输入的数：")
    for i in range(Len):
        c = int(input())
        a.append(c)
    #a=[3,10,12,6,1,32,8]
    print(Quick_Sort(a,0,len(a)-1))
