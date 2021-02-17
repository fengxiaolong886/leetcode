'''
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

'''

def maxProfit(prices, fee):
    dp = [[0 for i in prices] for _ in range(2)]
    dp[0][0] = -prices[0]
    dp[1][0] = 0
    for i in range(1, len(prices)):
        # buy
        dp[0][i] = max(dp[1][i-1] - prices[i], dp[0][i-1])
        # sell
        dp[1][i] = max(dp[0][i-1] + prices[i] - fee, dp[1][i-1])
    return dp[1][-1]

print(maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))
