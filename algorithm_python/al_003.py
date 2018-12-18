#!/usr/bin/python3
import sys
import math
import time
import random
import matplotlib.pyplot as plt

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
L = []
def random_List(Length):
    start=-500
    end  =+500
    for i in range(Length):
        L.append({"x":random.randint(start,end),"y":random.randint(start,end)})
    return L
def get_base(L): #查找左下角的点
    k = 0
    for i in range(1,len(L)):
        if L[i]['y']<L[k]['y'] or (L[i]['y']==L[k]['y']and L[i]['x']<L[k]['x']):
            k = i
    return k
def multiply(p1,p2,p0):#求叉乘
    return (p1['x']-p0['x'])*(p2['y']-p0['y'])-(p1['y']-p0['y'])*(p2['x']-p0['x'])
def arc(p1,p0):
    #求出极角用来排序
    if(p1['x']-p0['x']) == 0:
        if(p1['y']-p0['y']==0):
            return -1 #相同的数
        else:
            return math.pi/2
    tan = float((p1['y']-p0['y']))/float((p1['x']-p0['x']))
    arc = math.atan(tan)
    if arc >= 0:
        return arc
    else:
        return math.pi+arc
def sort_points(L,k):#排序
    p2 = []
    for i in range(0,len(L)):
        p2.append({"index":i,"arc":arc(L[i],L[k])})
    p2.sort(key=lambda k: (k.get('arc',0)))
    p_out = []
    for i in range(0,len(p2)):
        p_out.append(L[p2[i]["index"]])
    return p_out
def graham_scan(p):
    k = get_base(L)
    p_sort = sort_points(L, k)
    p_result = [None] * len(p_sort)
    p_result[0] = p_sort[0]
    p_result[1] = p_sort[1]
    p_result[2] = p_sort[2]

    top = 2
    for i in range(3, len(p_sort)):
        #叉乘为正则符合条件
        while (top >= 1 and multiply(p_sort[i], p_result[top], p_result[top - 1]) > 0):
            top -= 1
        top += 1
        p_result[top] = p_sort[i]
    for i in range(len(p_result) - 1, -1, -1):
        if p_result[i] == None:
            p_result.pop()
    for i in range(0,len(p_result)):
        x2.append(p_result[i]['x'])
        y2.append(p_result[i]['y'])
    for i in range(len(L)):
        x1.append(L[i]['x'])
        y1.append(L[i]['y'])
    x3.append(p_result[0]['x'])
    y3.append(p_result[0]['y'])
    x3.append(p_result[len(p_result)-1]['x'])
    y3.append(p_result[len(p_result)-1]['y'])
    plt.scatter(x1, y1, color='b')
    plt.plot(x2, y2, color='r', linewidth=1, alpha=0.6)
    plt.plot(x3,y3,color='r')
    plt.show()
    return p_result
def area(p_result):
    area = 0
    for i in range(0,len(p_result)-2):
        area= area+float(multiply(p_result[0],p_result[i+1],p_result[i+2]))/2
    print("多边形的最大面积为：")
    print(area)
    #return area
def main():
    x1.clear()
    y1.clear()
    x2.clear()
    y2.clear()
    x3.clear()
    y3.clear()
    L.clear()
    random_List(4)
    #get_base(L)
    print(graham_scan(L))
    area(graham_scan(L))