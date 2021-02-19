"""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。
"""

def numIdenticalPairs(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                res += 1
    return res


print(numIdenticalPairs(nums = [1,2,3,1,1,3]))
print(numIdenticalPairs(nums = [1,1,1,1]))
print(numIdenticalPairs(nums = [1,2,3]))