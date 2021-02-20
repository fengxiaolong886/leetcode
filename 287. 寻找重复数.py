"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

"""

def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            return nums[i]

print(findDuplicate(nums = [1,3,4,2,2]))
print(findDuplicate(nums = [3,1,3,4,2]))
print(findDuplicate(nums = [1,1]))
print(findDuplicate(nums = [1,1,2]))