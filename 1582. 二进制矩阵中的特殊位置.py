"""
给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。

特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。
"""

def numSpecial(mat):
    matchrow = []
    matchcol = []
    row, col = len(mat), len(mat[0])
    for i in range(row):
        if sum(mat[i]) == 1:
            matchrow.append(i)
    for i, j in enumerate(zip(*mat)):
        if sum(j) == 1:
            matchcol.append(i)
    res = 0
    for i in matchrow:
        for j in matchcol:
            if mat[i][j] == 1:
                res += 1
    return res

print(numSpecial(mat = [[1,0,0],
            [0,0,1],
            [1,0,0]]))
print(numSpecial(mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]))
print(numSpecial(mat = [[0,0,0,1],
[1,0,0,0],
[0,1,1,0],
[0,0,0,0]]))
print(numSpecial(mat = [[0,0,0,0,0],
[1,0,0,0,0],
[0,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]]))