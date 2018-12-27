#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
graph = {
        '0': {'2': -20, '4': 30, '5': 100},
        '1': {'2': 5},
        '2': {'3': -50},
        '3': {'5': 10},
        '4': {'3': 20},
        '5': {'4': -60}
    }
'''

#具有环路的graph
graph = {
        '0': {'1': -1,'2':4},
        '1': {'2': 2,'3':3,'4':2},
        '2': {},
        '3': {'1':3},
        '4': {'3':-5},
        '5': {}
}

def bellman_ford(graph, source):
    dist = {}
    p = {}
    max = 10000
    for v in graph:
        dist[v] = max  # 赋值为负无穷完成初始化
        p[v] = -1
    dist[source] = 0

    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    p[v] = u  # 完成松弛操作，p为前驱节点

    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return [],[100001] # 判断是否存在环路

    return dist, p

def test(start, end, graph):
    start = str(start)
    end = str(end)

    dist, Path = bellman_ford(graph, start)
    if len(Path) ==0:
        return []
    if len(Path) ==1:
        return [100001]
    minpath = []
    if Path[end] == start:
        minpath.append(int(end))
        minpath.append(int(start))
    elif Path[end] != start and Path[end] != -1:
        minpath.append(int(end))
        bef = Path[end]
        while (bef != -1 and bef != start):
            minpath.append(int(bef))
            bef = Path[bef]
        if bef == -1:
            return []
        minpath.append(int(start))
    return minpath[::-1]

if __name__ == '__main__':

    for i in range(5):
        for j in range(5):
            print(test(i, j, graph))

