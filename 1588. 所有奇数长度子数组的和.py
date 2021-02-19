"""
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。
"""
def sumOddLengthSubarrays(arr):
    res = 0
    for p1 in range(len(arr)):
        p2 = 0
        while p1 + p2 +1 <= len(arr):
            res += sum(arr[p1:p1+p2+1])
            p2 += 2
    return res


print(sumOddLengthSubarrays(arr = [1,4,2,5,3]))
print(sumOddLengthSubarrays(arr = [1,2]))
print(sumOddLengthSubarrays(arr = [10,11,12]))