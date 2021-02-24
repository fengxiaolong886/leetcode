"""
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi]
表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。
"""
from collections import Counter
def destCity(paths):
    total = []
    end = []
    for (i, j) in paths:
        total.append(i)
        total.append(j)
        end.append(j)
    totaldict = Counter(total)
    for i in totaldict:
        if totaldict[i] == 1 and i in end:
            return i

print(destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity(paths = [["B","C"],["D","B"],["C","A"]]))
print(destCity(paths = [["A","Z"]]))