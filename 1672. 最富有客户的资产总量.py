"""

给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。

客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。
"""


def maximumWealth(accounts):
    res = 0
    for i in accounts:
        res = max(res, sum(i))
    return res

print(maximumWealth(accounts = [[1,2,3],[3,2,1]]))
print(maximumWealth(accounts = [[1,5],[7,3],[3,5]]))
print(maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))