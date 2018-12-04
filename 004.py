#!/usr/bin/python3
import math
import sys
a=float('inf')
b={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
matrix = [[0, 4, 3, 12,a, 3],
          [4, 0, a, a, 6, 1],
          [3, a, 0, 10,a, a],
          [12,a, 10,0, 2, 4],
          [a, 6, a, 2, 0, a],
          [3, 1, a, 4, a, 0],
          ]
def prim(matrix,n):
    treeDis = matrix[0]  # 各个点距离生成树的最短距离列表
    visited = [0 for i in range(6)]  # 已经访问过的节点将被置为1
    visited[0] = 1
    minDistance = 0
    # 不在树中的点距离树有最短距离，在树中对应的距离最小的那个点
    # 比如neighbor[1]=0表示在节点1还不在树中时，它离树中的节点0距离最小
    neighbor = [0] * 6
    for i in range(5):
        minDis = a
        # 找出此时离树距离最小的不在树中顶点
        for j in range(6):
            if (not visited[j]) and (treeDis[j] < minDis):
                minDis = treeDis[j]
                minDisPos = j
        minDistance+=minDis
        visited[minDisPos] = 1
        print(b[minDisPos], minDis)
        for j in range(6):
            # 刷新剩下的顶点距离树的最短距离
           if (not visited[j]) and (matrix[minDisPos][j] < treeDis[j]):
                treeDis[j] = matrix[minDisPos][j]
                neighbor[j] = minDisPos
        # print("Here minDIsPos : "+str(minDisPos))
    print(neighbor)
    print("The minmum distance are:")
    print(minDistance)
    print("Edges that in the tree:")
    for i in range(1, 6):
        print(b[int(str(i))] + '-' + b[int(str(neighbor[i]))])
def main():
    n=6
    prim(matrix, n)
main()
