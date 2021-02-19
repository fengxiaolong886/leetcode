"""
给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。
"""

def kidsWithCandies(candies, extraCandies):
    maxcandies = max(candies)
    res = []
    for i in candies:
        if i + extraCandies >= maxcandies:
            res.append(True)
        else:
            res.append(False)
    return res

print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(kidsWithCandies(candies = [12,1,12], extraCandies = 10))