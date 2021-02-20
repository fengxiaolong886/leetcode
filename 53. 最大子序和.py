"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""

def maxSubArray(nums):
    if len(nums) == 1:return nums[0]
    res = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            res = max(res, sum(nums[i:j+1]))
    return res

print(maxSubArray(nums = [-2,1]))
print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray(nums = [1]))
print(maxSubArray(nums = [0]))
print(maxSubArray(nums = [-1]))
print(maxSubArray(nums = [-100000]))

