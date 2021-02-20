"""
 n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。

每 3 个士兵可以组成一个作战单位，分组规则如下：

从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。
"""
from itertools import combinations
def numTeams(rating):
    res = 0
    for (i, j, k) in combinations(rating, 3):
        if i > j > k or i<j<k:
            res += 1
    return res

print(numTeams(rating = [2,5,3,4,1]))
print(numTeams(rating = [2,1,3]))
print(numTeams(rating = [1,2,3,4]))