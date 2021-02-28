"""
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。
"""

def xorOperation(n, start):
    s = [start + 2* i for i in range(n)]
    res = s[0]
    for i in s[1:]:
        res ^= i
    return res


print(xorOperation(n = 5, start = 0))
print(xorOperation(n = 4, start = 3))
print(xorOperation(n = 1, start = 7))
print(xorOperation(n = 10, start = 5))
