"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，

能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
"""

def canPlaceFlowers(flowerbed, n):
    res = 0
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            res += 1
    else:
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            res += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            res += 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i +1] == 0:
                res += 1
                flowerbed[i] = 1
    return res >= n

print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))