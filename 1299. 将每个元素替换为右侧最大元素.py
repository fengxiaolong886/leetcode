"""
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

完成所有替换操作后，请你返回这个数组。
"""

def replaceElements(arr):
    res = []
    for i in range(len(arr)-1):
        res.append(max(arr[i+1:]))
    res.append(-1)
    return res

print(replaceElements(arr = [17,18,5,4,6,1]))
print(replaceElements(arr = [400]))