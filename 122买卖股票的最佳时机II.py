'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''

def maxProfit(prices):
    dp = [[0 for i in prices] for _ in range(2)]
    dp[0][0] = -prices[0]
    dp[1][0] = 0
    for i in range(1, len(prices)):
        # buy
        dp[0][i] = max(dp[1][i-1] - prices[i], dp[0][i-1])
        # sell
        dp[1][i] = max(dp[0][i-1] + prices[i], dp[1][i-1])
    return dp[1][-1]

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))