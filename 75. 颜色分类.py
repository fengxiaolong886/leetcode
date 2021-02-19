'''

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色
'''

def sortColors(nums):
    nums.sort()
    return nums

print(sortColors(nums = [2,0,2,1,1,0]))
print(sortColors(nums = [2,0,1]))
print(sortColors(nums = [0]))
print(sortColors(nums = [1]))