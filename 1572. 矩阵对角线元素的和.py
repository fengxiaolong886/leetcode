"""
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
"""

def diagonalSum(mat):
    n = len(mat)
    res = 0
    for i in range(n):
        res += mat[i][i]
    for i in range(n):
        res += mat[i][n-i-1]
    if n%2 == 1:
        loc = int(n/2)
        res -= mat[loc][loc]
    return res


print(diagonalSum(mat = [[1,2,3], [4,5,6], [7,8,9]]))
print(diagonalSum(mat = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))
print(diagonalSum(mat = [[5]]))