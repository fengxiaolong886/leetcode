"""

给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。

"""

from collections import Counter
def leastInterval(tasks, n):
    taskdict = Counter(tasks)
    temp = []
    tasklist= []
    for i in taskdict:
        temp.append(taskdict[i])
        tasklist.append(i)
    maxiumLengthTask = max(temp)
    counterofmax = 0
    for i in temp:
        if i == maxiumLengthTask:
            counterofmax += 1

    timesquare =(maxiumLengthTask -1) * (n + 1)
    return max(len(tasks), timesquare + counterofmax)

print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))