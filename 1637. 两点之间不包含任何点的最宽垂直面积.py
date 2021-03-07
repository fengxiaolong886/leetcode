"""
给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直面积 的宽度。

垂直面积 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直面积 为宽度最大的一个垂直面积。

请注意，垂直区域 边上 的点 不在 区域内。

"""

def maxWidthOfVerticalArea(points):
    points.sort()
    res = 0
    n = len(points)
    for i in range(1, n):
        # print(points[i][0])
        res = max(points[i][0] - points[i-1][0], res)
    return res

print(maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
print(maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))