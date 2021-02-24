"""
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。
"""
from collections import Counter
def sumOfUnique(nums):
    couts = Counter(nums)
    res = 0
    for (i, j) in couts.items():
        # print(i, j)
        if j ==1:
            res += i
    return res

print(sumOfUnique([1,2,3,2]))
print(sumOfUnique([1,1,1,1,1]))
print(sumOfUnique([1,2,3,4,5]))