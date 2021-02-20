"""
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
"""

def minCostClimbingStairs(cost):
    dp = [0 for i in cost]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1] , dp[i-2]) + cost[i]
    return min(dp[-1], dp[-2])


print(minCostClimbingStairs(cost = [10, 15, 20]))
print(minCostClimbingStairs(cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))