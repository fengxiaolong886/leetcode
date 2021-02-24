"""
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
"""

def maxScore(cardPoints, k):
    n = len(cardPoints)
    w = n - k
    s = sum(cardPoints[:w])
    res = s
    for i in range(w, n):
        s += cardPoints[i] - cardPoints[i - w]
        res = min(res, s)
    return sum(cardPoints) - res


print(maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
print(maxScore(cardPoints = [2,2,2], k = 2))
print(maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
print(maxScore(cardPoints = [1,1000,1], k = 1))
print(maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3))