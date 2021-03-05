"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
"""

def isPowerOfFour(n):
    if n < 1:
        return False
    while n > 1:
        if n % 4 == 0:
            n = n // 4
        else:
            return False
    return True

print(isPowerOfFour(4))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
print(isPowerOfFour(-2147483648))

