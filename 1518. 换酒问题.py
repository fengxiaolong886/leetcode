"""
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。
"""

def numWaterBottles(numBottles, numExchange):
    res = numBottles
    full = numBottles
    while full >= numExchange:
        full, empty = divmod(full, numExchange)
        res += full
        full = full + empty
    return res


print(numWaterBottles(numBottles = 9, numExchange = 3))
print(numWaterBottles(numBottles = 15, numExchange = 4))
print(numWaterBottles(numBottles = 5, numExchange = 5))
print(numWaterBottles(numBottles = 2, numExchange = 3))