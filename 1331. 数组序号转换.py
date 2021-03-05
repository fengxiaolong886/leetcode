"""
给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。
"""
def arrayRankTransform(arr):
    query = list(set(arr))
    query.sort()
    rank = {}
    for idx, c in enumerate(query):
        rank[c] = idx + 1
    for i in range(len(arr)):
        arr[i] = rank[arr[i]]
    return arr

print(arrayRankTransform(arr = [40,10,20,30]))
print(arrayRankTransform(arr = [100,100,100]))
print(arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))