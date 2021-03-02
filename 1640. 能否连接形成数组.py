"""
给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。

如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false
"""
def canFormArray(arr, pieces):
    res = []
    for i in arr:
        for j in pieces:
            if i == j[0]:
                res.extend(j)
    return res == arr

print(canFormArray(arr = [85], pieces = [[85]]))
print(canFormArray(arr = [15,88], pieces = [[88],[15]]))
print(canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
print(canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
print(canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]]))

