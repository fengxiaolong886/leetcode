"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from itertools import combinations

def subsets(nums):
    res = []
    n = len(nums)
    for i in range(n+1):
        for j in combinations(nums, i):
            res.append(list(j))
    return res

print(subsets(nums = [1,2,3]))
