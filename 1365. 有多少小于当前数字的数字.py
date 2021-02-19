"""
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。
"""

def smallerNumbersThanCurrent(nums):
    res = []
    for i in nums:
        ans = 0
        for j in nums:
            if j < i:
                ans += 1
        res.append(ans)
    return res

print(smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
print(smallerNumbersThanCurrent(nums = [6,5,4,8]))
print(smallerNumbersThanCurrent(nums = [7,7,7,7]))