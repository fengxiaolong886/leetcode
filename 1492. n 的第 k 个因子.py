"""
给你两个正整数 n 和 k 。

如果正整数 i 满足 n % i == 0 ，那么我们就说正整数 i 是整数 n 的因子。

考虑整数 n 的所有因子，将它们 升序排列 。请你返回第 k 个因子。如果 n 的因子数少于 k ，请你返回 -1 。
"""

def kthFactor(n, k):
    res = []
    i = 1
    j = n
    res.append(i)
    res.append(j)
    while i < j:
        i += 1
        if n % i == 0:
            j = n//i
            res.append(i)
            res.append(j)
    res = sorted(set(res))
    if len(res) < k:
        return -1
    else:
        return res[k-1]



print(kthFactor(12, 3))
print(kthFactor(7, 2))
print(kthFactor(4, 4))
print(kthFactor(1, 1))
print(kthFactor(1000, 3))