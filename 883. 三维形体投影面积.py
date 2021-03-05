"""
在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。

"""

def projectionArea(grid):
    a1, a2, a3 = 0, 0, 0
    for i in grid:
        for j in i:
            if j != 0:
                a1 += 1
        a2 += max(i)
    for i in zip(*grid):
        a3 += max(i)
    return a1 + a2 + a3

print(projectionArea([[2]]))
print(projectionArea([[1,2],[3,4]]))
print(projectionArea([[1,0],[0,2]]))
print(projectionArea([[1,1,1],[1,0,1],[1,1,1]]))
print(projectionArea([[2,2,2],[2,1,2],[2,2,2]]))
