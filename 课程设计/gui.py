#!/usr/bin python
# -*- coding:utf-8 -*-
import numpy as np
import tkinter as tk
from pylab import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import *
import BellmanFord as bf


x = [3, 3, 6, 9, 9, 6]
y = [7, 4, 1, 4, 7, 10]
Port = [[3, 7], [3, 4], [6, 1], [9, 4], [9, 7], [6, 10]]


def _quit():
    """
    退出功能，暂时没用上
    :return:
    """
    root.quit()
    root.destroy()

def drawPic():
    """
    读取两个entry中的值，画路径-
    :return:
    """

    start = int(inputEntry1.get())          #读起点
    end = int(inputEntry2.get())            #读终点
    # 清空图像，以使得前后两次绘制的图像不会重叠
    R.clear()
    path = bf.test(start, end, bf.graph)               #将起点和终点输入进Bellman-Ford算法，得到path列表
    init_port(R)                            #初始化右图
    l = len(path)
    lenth = 0
    if l == 0:
        R.set_title("NO Path!")
    elif l ==1:
        R.set_title("It has a negative loop")
    else:
        for i in range(l-1):
            drawArrow1(Port[path[i]], Port[path[i+1]], R)
            lenth = lenth + bf.graph[str(path[i])][str(path[i+1])]
        R.set_title('The lenth is  ' + str(lenth))
    canvas.draw()

def drawArrow1(A, B,obj):
    """
    画箭头
    :param A:起点
    :param B: 终点
    :param obj: 对象，左图还是右图，L or R
    :return:
    """
    m = str(Port.index(A))
    n = str(Port.index(B))
    # 注意： 默认显示范围[0,1][0,1],需要单独设置图形范围，以便显示箭头
    obj.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]), arrowprops=dict(arrowstyle="->"))
    obj.annotate(bf.graph[m][n], ((A[0]+ B[0])/2, (A[1]+ B[1])/2))



def init_port(obj):
    """
    初始化一个图，将所有点画出来，并且标注
    :param obj: 对象，左图还是右图，L or R
    :return:
    """
    obj.clear()
    obj.set_xlim(0, 11)
    obj.set_ylim(0, 11)
    obj.axis('off')
    obj.axis('off')
    #a.set_title('带权有向图')
    area = 3.14*400
    obj.scatter(x, y, s=area, c='r', alpha=1, marker='o')
    for i in range(len(x)):
        obj.annotate(i, (x[i], y[i]))
    canvas.draw()

def draw_all_line(gra, obj):
    """
    将所有的线画出来
    :param obj: 对象，左图还是右图，L or R，一般只给左图用
    :return:
    """
    for i in gra:
        for j in gra[i]:
            drawArrow1(Port[int(i)], Port[int(j)], obj)
    canvas.draw()


if __name__ == '__main__':
    from matplotlib import *
    matplotlib.use('TkAgg')
    root = tk.Tk()                      #生成一个tk窗口命名为root
    root.title('算法课设')              #窗口标题

    # 在Tk的GUI上放置一个画布，并用.grid()来调整布局
    f = Figure(figsize=(10, 5), dpi=100)
    L = f.add_subplot(121)
    R = f.add_subplot(122)
    canvas = FigureCanvasTkAgg(f, master=root)
    init_port(L)
    init_port(R)
    draw_all_line(bf.graph, L)
    L.set_title('Figure')
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, columnspan=5, sticky=tk.E)

    # 放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
    tk.Label(root, text='源点：').grid(row=1, column=0,sticky=tk.E)
    tk.Label(root, text='终点：').grid(row=1, column=2,sticky=tk.E)
    inputEntry1 = tk.Entry(root)
    inputEntry1.grid(row=1, column=1, sticky=tk.W)
    inputEntry1.insert(0, '0')
    inputEntry2 = tk.Entry(root)
    inputEntry2.grid(row=1, column=3, sticky=tk.W)
    inputEntry2.insert(0, '0')

    tk.Button(root, text='画图', command=drawPic).grid(row=1, column=4, columnspan=3)
    # 启动事件循环
    root.mainloop()

