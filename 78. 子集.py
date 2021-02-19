"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""
import itertools
def subsets(nums):
    res = []
    for i in range(len(nums) + 1):
        total = itertools.combinations(nums, i)
        for i in list(total):
            res.append(list(i))
    return res

print(subsets(nums = [1,2,3]))
print(subsets(nums = [0]))