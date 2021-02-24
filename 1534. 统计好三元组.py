"""
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。

如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。

返回 好三元组的数量 。
"""
from itertools import combinations
def countGoodTriplets(arr, a, b, c):
    res = 0
    for(i, j, k) in combinations(arr, 3):
        if abs(i - j) <= a and abs(j-k) <=b and abs(i-k)<=c:
            res +=1
    return res

print(countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
print(countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))