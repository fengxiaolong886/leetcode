"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
"""


def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    row, column = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)
    for i in list(row):
        matrix[i] = [0 for _ in range(n)]
    for x in range(m):
        for i in column:
            matrix[x][i] = 0
    return matrix

print(setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
]))
print(setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))