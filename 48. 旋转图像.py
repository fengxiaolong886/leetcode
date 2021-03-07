"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

"""

def rotate(matrix):
    matrix[:] = [list(tup)[::-1] for tup in zip(*matrix)]

print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(rotate(matrix = [[1]]))
print(rotate(matrix = [[1,2],[3,4]]))