"""
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
"""

def findNumbers(nums):
    res = 0
    for i in nums:
        if len(str(i))%2 == 0:
            res += 1
    return res

print(findNumbers(nums = [12,345,2,6,7896]))
print(findNumbers(nums = [555,901,482,1771]))