"""
给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。

如果 nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。

源数组中可能存在 重复项 。

注意：我们称数组 A 在轮转 x 个位置后得到长度相同的数组 B ，当它们满足 A[i] == B[(i+x) % A.length] ，其中 % 为取余运算。
"""

def check(nums):
    checkpoint = 0
    for i in range(len(nums)):
        if nums[i] < nums[i-1]:
            checkpoint += 1
    return checkpoint < 2

print(check(nums = [3,4,5,1,2]))
print(check(nums = [2,1,3,4]))
print(check(nums = [1,2,3]))
print(check(nums = [1,1,1]))
print(check(nums = [2,1]))
print(check(nums = [1]))