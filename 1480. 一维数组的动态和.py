"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

"""

def runningSum(nums):
    res = []
    for i in range(1, len(nums)+1):
        res.append(sum(nums[:i]))
    return res

print(runningSum(nums = [1,2,3,4]))
print(runningSum(nums = [1,1,1,1,1]))
print(runningSum(nums = [3,1,2,10,1]))