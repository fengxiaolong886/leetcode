"""
有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：

每一轮中，你将会选出 任意 3 堆硬币（不一定连续）。
Alice 将会取走硬币数量最多的那一堆。
你将会取走硬币数量第二多的那一堆。
Bob 将会取走最后一堆。
重复这个过程，直到没有更多硬币。
给你一个整数数组 piles ，其中 piles[i] 是第 i 堆中硬币的数目。

返回你可以获得的最大硬币数目。
"""

def maxCoins(piles):
    piles.sort(reverse=True)
    res = []
    while piles:
        piles.pop(0)
        my = piles.pop(0)
        res.append(my)
        piles.pop()
    return sum(res)

print(maxCoins(piles = [2,4,1,2,7,8]))
print(maxCoins(piles = [2,4,5]))
print(maxCoins(piles = [9,8,7,6,5,1,2,3,4]))