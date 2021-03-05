"""

给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。

操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。

在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
"""
# from collections import Counter
# def maxCount(m, n, ops):
#     matrix = [[0 for i in range(m)] for _ in range(n)]
#     for i , j in ops:
#         for x in range(i):
#             for y in range(j):
#                 matrix[x][y] += 1
#     res = []
#     for i in range(m):
#         for j in range(n):
#             res.append(matrix[i][j])
#     maxvalue = max(res)
#     ans = 0
#     for i in res:
#         if i == maxvalue:
#             ans += 1
#     return ans


def maxCount(m, n, ops):
    if not ops:
        return m * n
    row = []
    col = []
    for i, j in ops:
        row.append(i)
        col.append(j)
    return min(row) * min(col)

print(maxCount(m = 3, n = 3, ops= [[2,2],[3,3]]))