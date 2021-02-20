"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
"""

def maxArea(height):
    n = len(height)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            res = max(res, min(height[i], height[j]) * (j - i))
    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
print(maxArea([4,3,2,1,4]))
print(maxArea([1,2,1]))