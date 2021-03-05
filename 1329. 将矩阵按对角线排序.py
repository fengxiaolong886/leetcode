"""
矩阵对角线 是一条从矩阵最上面行或者最左侧列中的某个元素开始的对角线，沿右下方向一直到矩阵末尾的元素。例如，矩阵 mat 有 6 行 3 列，从 mat[2][0] 开始的 矩阵对角线 将会经过 mat[2][0]、mat[3][1] 和 mat[4][2] 。

给你一个 m * n 的整数矩阵 mat ，请你将同一条 矩阵对角线 上的元素按升序排序后，返回排好序的矩阵。
"""
from collections import defaultdict
def diagonalSort(mat):
    row ,col = len(mat), len(mat[0])
    diag = defaultdict(list)
    for i in range(col):
        m, n = 0, i
        while m < row and n < col:
            diag[(0, i)].append(mat[m][n])
            m += 1
            n += 1
    for i in range(1, row):
        m, n = i, 0
        while m < row and n < col:
            diag[(i, 0)].append(mat[m][n])
            m += 1
            n += 1
    for i in diag:
        diag[i] = sorted(diag[i])
    for i in diag:
        m, n = i
        for x in diag[i]:
            mat[m][n] = x
            m += 1
            n += 1
    return mat


print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print(diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))