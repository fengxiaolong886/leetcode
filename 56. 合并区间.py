'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
'''

def merge(intervals):
    intervals.sort()
    res = []
    res.append(intervals[0])
    for i in intervals:
        merged = res[-1]
        if merged[0] <= i[0] <= merged[1] and i[1] >= merged[1]:
            res[-1][1] = i[1]
        if i[0] > merged[1]:
            res.append(i)
    return res


print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(merge(intervals = [[1,4],[4,5]]))