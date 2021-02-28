"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from itertools import permutations

def permute(nums):
    res = []
    for i in permutations(nums, len(nums)):
        res.append(i)
    return res

print(permute([1,2,3]))