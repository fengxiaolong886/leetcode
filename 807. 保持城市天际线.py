def maxIncreaseKeepingSkyline(grid):
    m, n = len(grid), len(grid[0])
    row_h , col_h = [], []
    for i in grid:
        row_h.append(max(i))
    for i in zip(*grid):
        col_h.append(max(i))
    res = 0
    for i in range(m):
        for j in range(n):
            cur = grid[i][j]
            target = min(row_h[i], col_h[j])
            res += target-cur
            # grid[i][j] = target
    return res

print(maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

