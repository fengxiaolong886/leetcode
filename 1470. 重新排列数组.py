"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

"""

def shuffle(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

print(shuffle(nums = [2,5,1,3,4,7], n = 3))
print(shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(shuffle(nums = [1,1,2,2], n = 2))